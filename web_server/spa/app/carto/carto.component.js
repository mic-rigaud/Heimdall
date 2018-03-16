/**
 * @Author: michael
 * @Date:   10-Mar-2018
 * @Project: Blueberry
 * @Filename: carto.component.js
 * @Last modified by:   michael
 * @Last modified time: 16-Mar-2018
 * @License: GNU GPL v3
 */


angular.module('carto').component('carto', {
  templateUrl: 'spa/app/carto/carto.template.html',
  controller: ['$scope', '$interval', '$http',
    function CartoController($scope, $interval, $http) {
      var self = this;

      function getData() {
        $http.get('./api-v0.0/ip').then(function(response) {
          self.datafromapi = response.data;
          console.log(response.data)
        });
      }

      getData();

      // TODO: Cela creer des petits bugs d'affichage... a regler
      $interval(function() {
        getData();
      }, 10000);

      $scope.delete = function(ip, mac) {
        // TODO: Ajouter la suppression de l'elément
        console.log(ip)
      }

      $scope.changeConfiance = function(ip, mac) {
        // TODO: Ajouter modification de l element
        console.log(ip)
      }
    }
  ]
});
