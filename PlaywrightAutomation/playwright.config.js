// @ts-check
import { defineConfig, devices } from '@playwright/test';
import { trace } from 'node:console';
import { config } from 'node:process';

/**
 * Read environment variables from file.
 * https://github.com/motdotla/dotenv
 */
// import dotenv from 'dotenv';
// import path from 'path';
// dotenv.config({ path: path.resolve(__dirname, '.env') });

/**
 * @see https://playwright.dev/docs/test-configuration
 */
const Config = ({
  testDir: './tests',
  // timeout : 40 * 1000 ,
  expect : {
     timeout : 5 * 1000 , 
  },
  reporter : 'html',

  use: {
     browserName : 'chromium' ,  //firefox' 'chromium' // webkit = safari

    // instead of --head use 

      headless : false  ,  // true :webpage will not open    //false - webage will open
      
      Screenshot : 'on',
      trace : 'on'    // 'retain-on-failure'
  },

  
});

module.exports = Config

