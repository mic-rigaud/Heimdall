// Boostraping env
var env = {};
if(window){
  Object.assign(env, window.__env);
}

// Create module and attach env
var NodeChain = angular.module('NodeChain', ['ngRoute','angularCSS']);
NodeChain.constant('__env', env);


NodeChain.config(function($routeProvider) {
  $routeProvider

  .when('/carto', {
    templateUrl : 'spa/angular/carto/page.html',
    controller  : 'PageCtrl'
  })

  .when('/outils', {
      templateUrl : 'spa/angular/outils/page.html',
      controller  : 'PageCtrl'
  })

  .when('/fiches-reflexes', {
      templateUrl : 'spa/angular/fiches-reflexes/page.html',
      controller  : 'PageCtrl'
  })

  .when('/configuration', {
      templateUrl : 'spa/angular/configuration/page.html',
      controller  : 'PageCtrl'
  })

  .when('/',{
    templateUrl : 'spa/angular/index/index.html',
    controller  : 'IndexCtrl'
  })

  .otherwise({redirectTo: '/'});
});
