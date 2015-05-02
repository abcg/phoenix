eventosModule.config(function ($routeProvider) {
    $routeProvider.when('/VPortada', {
                controller: 'VPortadaController',
                templateUrl: 'app/login/VPortada.html'
            });
});

eventosModule.controller('VPortadaController', 
   ['$scope', '$location', '$route', 'flash', 'adminService', 'loginService', 'usuarioService',
    function ($scope, $location, $route, flash, adminService, loginService, usuarioService) {
      $scope.msg = '';
      loginService.VPortada().then(function (object) {
        $scope.res = object.data;
        for (var key in object.data) {
            $scope[key] = object.data[key];
        }
        if ($scope.logout) {
            $location.path('/');
        }
      });
      $scope.AIdentificar0 = function(login, clave) {
          
        loginService.AIdentificar({"login, clave":((typeof login, clave === 'object')?JSON.stringify(login, clave):login, clave)}).then(function (object) {
          var msg = object.data["msg"];
          if (msg) flash(msg);
          var label = object.data["label"];
          if (label == '/VPortada') {
              $route.reload();
          } else {
              $location.path(label);
          }
        });};

    }]);
