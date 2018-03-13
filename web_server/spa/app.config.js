/**
 * @Date:   17-Feb-2018
 * @Project: Blueberry
 * @Last modified time: 13-Mar-2018
 * @License: GNU GPL v3
 */



var Blueberry = angular.module('Blueberry');


Blueberry.config(function($locationProvider, $routeProvider) {
  $locationProvider.hashPrefix('!');

  $routeProvider
    .when('/carto', {
      template: '<carto></carto>'
    })

    .when('/outils', {
      template: '<outils></outils>',
    })

    .when('/fiches-reflexes', {
      template: '<fiches-reflexes></fiches-reflexes>',
    })

    .when('/configuration', {
      template: '<configuration></configuration>',
    })

    .when('/', {
      template: '<home></home>',
    })

    .otherwise({
      redirectTo: '/'
    });
});
