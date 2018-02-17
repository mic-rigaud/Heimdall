var NodeChain = angular.module('NodeChain');

NodeChain.controller("NavCtrl", function($scope,$location) {
   $scope.isActive = function (viewLocation) {
        return viewLocation === $location.path();
    };
})