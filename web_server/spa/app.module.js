/**
 * @Author: michael
 * @Date:   10-Mar-2018
 * @Project: Blueberry
 * @Filename: app.module.js
 * @Last modified by:   michael
 * @Last modified time: 13-Mar-2018
 * @License: GNU GPL v3
 */

// Boostraping env
var env = {};
if (window) {
  Object.assign(env, window.__env);
}

// Create module and attach env
var Blueberry = angular.module('Blueberry', ['ngRoute', 'angularCSS', 'carto', "configuration", "fiches-reflexes", "home", "outils"]);


Blueberry.constant('__env', env);
