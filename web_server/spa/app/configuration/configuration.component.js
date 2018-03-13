/**
 * @Author: michael
 * @Date:   13-Mar-2018
 * @Project: Blueberry
 * @Filename: configuration.module.js
 * @Last modified by:   michael
 * @Last modified time: 13-Mar-2018
 * @License: GNU GPL v3
 */


angular.module('configuration').component('configuration', {
  templateUrl: 'spa/app/configuration/configuration.template.html',
  controller: ['$scope', '$location', '$http',
    function CartoController($scope, $location, $http) {
      var self = this;

      $http.get('./api-v0.0/parametre').then(function(response) {
        self.datafromapi = response.data;
      });
    }
  ]
});
