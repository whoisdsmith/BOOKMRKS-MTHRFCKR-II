# MEGA Tools

---

![](https://opengraph.githubassets.com/77f04dcf63f14db831d98950d1ea8196c737115b0dde65f571183d3272aea792/ZonD80/mega-downloader)

- [mega-downloader](https://github.com/ZonD80/mega-downloader) - PHP script to download files and folders from mega.nz - GitHub - ZonD80/mega-downloader: PHP script to download files and folders from mega.nz

2022-11-14T16:19:35.000Z

#mega #tools

![](https://opengraph.githubassets.com/62b9cf820185e721964791e8f588300e3aa682f02d3828ff5da0fc62bc3e4a56/maybecryptic/MegaKeep)

- [MegaKeep](https://github.com/xCryptic/MegaKeep) - Log into multiple mega.nz accounts to keep files from being deleted - GitHub - xCryptic/MegaKeep: Log into multiple mega.nz accounts to keep files from being deleted

2022-11-14T16:19:30.000Z

#mega #tools

![](https://opengraph.githubassets.com/497acf6c2cfc33be2079f02c9d206df135bca71d579ff9f182501f041ae396f0/tonikelope/megadown)

- [megadown](https://github.com/tonikelope/megadown) - Bash script for download files from mega.nz and megacrypter - GitHub - tonikelope/megadown: Bash script for download files from mega.nz and megacrypter

2022-11-14T16:19:26.000Z

#mega #tools

![](https://opengraph.githubassets.com/ec1c7192182b352e6b1c3a8477296112bfa836d5f91d8a1e16f40affba6b01bd/Titoot/mega-checker)

- [mega-checker](https://github.com/Titoot/mega-checker) - check if mega links are valid or not (either one link or a txt file) - GitHub - Titoot/mega-checker: check if mega links are valid or not (either one link or a txt file)

2022-11-14T16:19:12.000Z

#mega #tools

![](https://opengraph.githubassets.com/b461aad540093dc2cd41fdceb20c5ffd6348b0d5a40ea6fdc7111596ef58cab8/JohnDeved/megacrypt.js)

- [megacrypt.js](https://github.com/JohnDeved/megacrypt.js) - just a concept for now. Contribute to JohnDeved/megacrypt.js development by creating an account on GitHub.

2022-11-14T16:19:04.000Z

#mega #tools

![](https://opengraph.githubassets.com/93bdcc959b8c59e6d030dd1484bf3a9f89a4da8457e3a27be01d41578b16c735/Cyberavater/Mega-Import-Bypass)

- [Mega-Import-Bypass](https://github.com/Cyberavater/Mega-Import-Bypass) - Contribute to Cyberavater/Mega-Import-Bypass development by creating an account on GitHub.

2022-11-14T16:18:50.000Z

#mega #tools

![](https://opengraph.githubassets.com/6fc91b6b6e176897142a0219f9ba3615ff167ae463933b86213a15284c06af44/crackhub-dev/mega-account-generator)

- [mega-account-generator](https://github.com/crackhub-dev/mega-account-generator) - Contribute to crackhub-dev/mega-account-generator development by creating an account on GitHub.

2022-11-14T16:18:46.000Z

#mega #tools

![](https://opengraph.githubassets.com/4a70d21833ede4ea72282906f6bb1f269f340309d0607bcadcbb9d834c729e6b/menukaonline/Mega-to-Google-Drive)

- [Mega-to-Google-Drive](https://github.com/cheems/Mega-to-Google-Drive) - This is a Google Colab notebook that helps you to transfer files from Mega to Google Drive - GitHub - cheems/Mega-to-Google-Drive: This is a Google Colab notebook that helps you to transfer files f...

2022-11-14T16:18:41.000Z

#mega #tools

![](https://opengraph.githubassets.com/2fd7b6cde66e852ba73d5feccc266b815b27d07a3609c713ec4dba6c22a11bda/3ncod3/keep-mega-alive)

- [keep-mega-alive](https://github.com/3ncod3/keep-mega-alive) - A script to keep your mega account(s) alive . Contribute to 3ncod3/keep-mega-alive development by creating an account on GitHub.

2022-11-14T16:18:36.000Z

#mega #tools

![](https://colab.research.google.com/img/colab_favicon_256px.png)

- [qBittorrent-MEGA.ipynb - Colaboratory](https://colab.research.google.com/github/Xavy-13/qbittorrent/blob/main/qBittorrent_MEGA.ipynb) - 

2022-11-14T16:18:07.000Z

#mega #tools

![](https://rdl.ink/render/https%3A%2F%2Fmegaddl.net)

- [Megaddl - Index page](https://megaddl.net) - 

2022-11-14T16:17:56.000Z

#mega #tools

![](https://katb.in/favicon.ico)

- [Katbin - atoyuxomuba](https://katb.in/atoyuxomuba) - // ==UserScript== // @name         MEGA.nz Ultimately Import // @name:zh-TW   MEGA.nz Ultimately Import / // @name:zh-CN   MEGA.nz Ultimately Import // @namespace    methusela // @version      0.1 // @description  Bypass import limit on Mega Web client & remove warning about the space usage // @author       d0gkiller87 // @match        chrome-extension://bigefpfhnfcobdlfbedofhhaibnlghod/* // @match        http://mega.co.nz/* // @match        http://mega.io/* // @match        http://mega.is/* // @match        http://mega.nz/* // @match        https://mega.co.nz/* // @match        https://mega.io/* // @match        https://mega.is/* // @match        https://mega.nz/* // @icon         https://mega.nz/favicon.ico?v=3 // @run-at       document-end // @grant        none // ==/UserScript==  (function() {     'use strict';     // Reference [Augular loaded detect]: https://stackoverflow.com/a/31970556/9182265     var initWatcher = setInterval(function () {         if (window.MegaUtils) {             clearInterval(initWatcher);             hookImport();             hookFull();             console.info('FUNtions Hooked!');         }     }, 500); })();  var hookImport = function () {     MegaUtils.prototype.checkGoingOverStorageQuota = function(opSize) {         var promise = new MegaPromise();         loadingDialog.pshow();          M.getStorageQuota()             .always(function() {             loadingDialog.phide();         })             .fail(promise.reject.bind(promise))             .done(function(data) {              /*             if (opSize === -1) {                 opSize = data.mstrg;             }              if (opSize  data.mstrg - data.cstrg) {                 var options = {custom: 1, title: l[882], body: l[16927]};                  M.showOverStorageQuota(data, options)                     .always(function() {                     promise.reject();                 });             }             else {             */             promise.resolve();         });         return promise;     }; }  var hookFull = function () {     FileManager.prototype.showOverStorageQuota = null; }

2022-11-14T16:17:46.000Z

#mega #tools

---

