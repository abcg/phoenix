eventosModule.config(function ($routeProvider) {
    $routeProvider.when('/VPortada', {
                controller: 'VPortadaController',
                templateUrl: 'app/login/VPortada.html'
            }).when('/VRegistroUsuario', {
                controller: 'VRegistroUsuarioController',
                templateUrl: 'app/login/VRegistroUsuario.html'
            });
});

eventosModule.controller('VPortadaController', 
   ['$scope', '$location', '$route', 'flash', 'adminService', 'loginService', 'usuarioService',
    function ($scope, $location, $route, flash, adminService, loginService, usuarioService) {
      $scope.msg = '';
      $scope.loginForm = {};

      loginService.VPortada().then(function (object) {
        $scope.res = object.data;
        for (var key in object.data) {
            $scope[key] = object.data[key];
        }
        if ($scope.logout) {
            $location.path('/');
        }
      });
      $scope.VRegistroUsuario1 = function() {
        $location.path('/VRegistroUsuario');
      };

      $scope.loginFormSubmitted = false;
      $scope.AIdentificar0 = function(isValid) {
        $scope.loginFormSubmitted = true;
        if (isValid) {
          
          loginService.AIdentificar($scope.loginForm).then(function (object) {
              var msg = object.data["msg"];
              if (msg) flash(msg);
              var label = object.data["label"];
              if (label == '/VPortada') {
                  $route.reload();
              } else {
                  $location.path(label);
              }
          });
        }
      };

    }]);
eventosModule.controller('VRegistroUsuarioController', 
   ['$scope', '$location', '$route', 'flash', 'adminService', 'loginService', 'usuarioService',
    function ($scope, $location, $route, flash, adminService, loginService, usuarioService) {
      $scope.msg = '';
      $scope.registroUsuarioForm = {'esAdministrador' : false};

      loginService.VRegistroUsuario().then(function (object) {
        $scope.res = object.data;
        for (var key in object.data) {
            $scope[key] = object.data[key];
        }
        if ($scope.logout) {
            $location.path('/');
        }
      });
      $scope.VPortada0 = function() {
        $location.path('/VPortada');
      };
      $scope.registroUsuarioFormSubmitted = false;
      $scope.ARegistrarUsuario0 = function(isValid) {
        $scope.registroUsuarioFormSubmitted = true;
        if (isValid) {
          
          loginService.ARegistrarUsuario($scope.registroUsuarioForm).then(function (object) {
              var msg = object.data["msg"];
              if (msg) flash(msg);
              var label = object.data["label"];
              if (label == '/VRegistroUsuario') {
                  $route.reload();
              } else {
                  $location.path(label);
              }
          });
        }
      };

    }]);
