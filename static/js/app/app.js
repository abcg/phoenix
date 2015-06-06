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
eventosModule.directive('file', function () {
    return {
        restrict: 'A',
        scope: {
            file: '='
        },
        link: function (scope, el, attrs) {
            el.bind('change', function (event) {
                var file = event.target.files[0];
                scope.file = file ? file : undefined;
                scope.$apply();
            });
        }
    };
});
