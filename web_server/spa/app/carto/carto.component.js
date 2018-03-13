/**
 * @Author: michael
 * @Date:   10-Mar-2018
 * @Project: Blueberry
 * @Filename: carto.component.js
 * @Last modified by:   michael
 * @Last modified time: 13-Mar-2018
 * @License: GNU GPL v3
 */


angular.module('carto').component('carto', {
  templateUrl: 'spa/app/carto/carto.template.html',
  controller: ['$scope', '$location', '$http',
    function CartoController($scope, $location, $http) {
      var self = this;

      $http.get('./api-v0.0/ip').then(function(response) {
        self.datafromapi = response.data;
      });
    }
  ]
});
