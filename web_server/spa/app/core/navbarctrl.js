/**
 * @Date:   18-Jan-2018
 * @Project: Blueberry
 * @Last modified time: 22-Feb-2018
 * @License: GNU GPL v3
 */



var Blueberry = angular.module('Blueberry');

Blueberry.controller("NavCtrl", function($scope,$location) {
   $scope.isActive = function (viewLocation) {
        return viewLocation === $location.path();
    };
})
