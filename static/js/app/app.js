// Creación del módulo de la aplicación
var eventosModule = angular.module('eventos', ['ngRoute', 'ngAnimate', 'flash']);
eventosModule.config(function ($routeProvider) {
    $routeProvider
        .when('/', {
                controller: 'VPortadaController',
                templateUrl: 'app/login/VPortada.html'
            });
});
eventosModule.controller('eventosController_',  ['$scope', '$http', '$location',
function($scope) {
    $scope.title = "Diseno";
}]);
