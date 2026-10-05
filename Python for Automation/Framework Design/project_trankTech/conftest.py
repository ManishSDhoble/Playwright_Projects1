recordings_by_test = {}


from html import escape
from pathlib import Path
import re
import shutil

import pytest
from playwright.sync_api import Error as PlaywrightError
from playwright.sync_api import sync_playwright

try:
    from pytest_html import extras as pytest_html_extras
except ImportError:
    pytest_html_extras = None

from config import BASE_URL


@pytest.fixture
def page(request):
    recordings_dir = Path("recordings")
    recordings_dir.mkdir(exist_ok=True)

    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context(
            ignore_https_errors=True,
            record_video_dir=str(recordings_dir),
        )
        page = context.new_page()
        page.set_default_timeout(60000)
        page.set_default_navigation_timeout(60000)

        page.goto(BASE_URL, wait_until="commit")
        yield page

        video = page.video
        video_path = None
        try:
            context.close()
        except PlaywrightError:
            video = None

        if video is not None:
            try:
                video_path = video.path()
            except (PlaywrightError, OSError):
                pass
            if video_path and Path(video_path).exists():
                safe_name = re.sub(r"[^A-Za-z0-9_.-]+", "_", request.node.nodeid)
                recording_path = recordings_dir / f"{safe_name}.webm"
                try:
                    shutil.move(video_path, recording_path)
                except OSError:
                    pass
                else:
                    recordings_by_test[request.node.nodeid] = recording_path

        try:
            browser.close()
        except PlaywrightError:
            pass


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    extras = getattr(report, "extras", getattr(report, "extra", []))

    if report.when == "call" and report.failed:
        page = item.funcargs.get("page")
        if page:
            screenshots_dir = Path("screenshots")
            screenshots_dir.mkdir(exist_ok=True)
            file_name = screenshots_dir / f"{item.name}.png"
            try:
                page.screenshot(path=str(file_name), timeout=5000)
            except BaseException:
                pass
            else:
                if pytest_html_extras is not None:
                    extras.append(pytest_html_extras.image(str(file_name)))
            report.extras = extras


@pytest.hookimpl(optionalhook=True)
def pytest_html_results_table_header(cells):
    cells.append("<th>Recording</th>")


@pytest.hookimpl(optionalhook=True)
def pytest_html_results_table_row(report, cells):
    recording_path = recordings_by_test.get(report.nodeid)
    if not recording_path or not recording_path.exists():
        cells.append("<td>No recording</td>")
        return

    report_path = escape(recording_path.as_posix())
    cells.append(
        "<td>"
        "<video controls width='640' style='max-width: 100%;'>"
        f"<source src='{report_path}' type='video/webm'>"
        "Your browser does not support video playback."
        "</video>"
        "</td>"
    )
