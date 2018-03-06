/**
 * @Date:   17-Feb-2018
 * @Project: Blueberry
 * @Last modified time: 04-Mar-2018
 * @License: GNU GPL v3
 */



var NodeChain = angular.module('NodeChain');

NodeChain.service("http_rest", function($http) {
  this.get = function(addr) {
    var promise = $http.get(addr).
    then(function(response) {
      return response.data;
    });
    return promise;
  }
})


NodeChain.controller("CartoCtrl", function($scope, $location, http_rest) {
  http_rest.get('./api-v0.0/ip').then(function(response) {
    $scope.datafromapi = response
  });
})
