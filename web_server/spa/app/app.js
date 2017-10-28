// Boostraping env
var env = {};
if(window){
    Object.assign(env, window.__env);
}


// Create module and attach env
var Blueberry = angular.module('Blueberry', ['ngRoute','angularCSS','nvd3']);
Blueberry.constant('__env', env);


Blueberry.config(function($routeProvider) {
    $routeProvider

        .when('/', {
            templateUrl : 'spa/app/components/home/home.html',
            controller  : 'HomeCtrl'
        })

        .when('/settings', {
            templateUrl : 'spa/angular/poloniex/poloniex.html',
            controller  : 'PoloCtrl'
        })

        .when('/about', {
            templateUrl : 'spa/angular/portofolio/portofolio.html',
            controller  : 'PortofCtrl'
        })

        .otherwise({redirectTo: '/poloniex'});
});
