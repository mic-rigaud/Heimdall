/**
 * @Date:   17-Feb-2018
 * @Project: Blueberry
 * @Last modified time: 04-Mar-2018
 * @License: GNU GPL v3
 */



// Boostraping env
var env = {};
if (window) {
  Object.assign(env, window.__env);
}

// Create module and attach env
var NodeChain = angular.module('NodeChain', ['ngRoute', 'angularCSS']);
NodeChain.constant('__env', env);


NodeChain.config(function($routeProvider) {
  $routeProvider

    .when('/carto', {
      templateUrl: 'spa/angular/carto/page.html',
      controller: 'CartoCtrl'
    })

    .when('/outils', {
      templateUrl: 'spa/angular/outils/page.html',
      controller: 'OutilsCtrl'
    })

    .when('/fiches-reflexes', {
      templateUrl: 'spa/angular/fiches-reflexes/page.html',
      controller: 'FichesCtrl'
    })

    .when('/configuration', {
      templateUrl: 'spa/angular/configuration/page.html',
      controller: 'ConfigurationCtrl'
    })

    .when('/', {
      templateUrl: 'spa/angular/index/index.html',
      controller: 'IndexCtrl'
    })

    .otherwise({
      redirectTo: '/'
    });
});
