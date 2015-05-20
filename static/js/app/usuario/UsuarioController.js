eventosModule.config(function ($routeProvider) {
    $routeProvider.when('/VInicioUsuario', {
                controller: 'VInicioUsuarioController',
                templateUrl: 'app/usuario/VInicioUsuario.html'
            }).when('/VEventoUsuario/:idEvento', {
                controller: 'VEventoUsuarioController',
                templateUrl: 'app/usuario/VEventoUsuario.html'
            }).when('/VAficheUsuario', {
                controller: 'VAficheUsuarioController',
                templateUrl: 'app/usuario/VAficheUsuario.html'
            }).when('/VCertificadoUsuario', {
                controller: 'VCertificadoUsuarioController',
                templateUrl: 'app/usuario/VCertificadoUsuario.html'
            }).when('/VCredenciales/:idEvento', {
                controller: 'VCredencialesController',
                templateUrl: 'app/usuario/VCredenciales.html'
            });
});

eventosModule.controller('VInicioUsuarioController', 
   ['$scope', '$location', '$route', 'flash', 'loginService', 'usuarioService',
    function ($scope, $location, $route, flash, loginService, usuarioService) {
      $scope.msg = '';
      usuarioService.VInicioUsuario().then(function (object) {
        $scope.res = object.data;
        for (var key in object.data) {
            $scope[key] = object.data[key];
        }
        if ($scope.logout) {
            $location.path('/');
        }
      });
      $scope.VEventoUsuario0 = function(args) {
        $location.path('/VEventoUsuario/'+args);
      };
      $scope.ADesconectarseUsuario1 = function() {
          
        usuarioService.ADesconectarseUsuario().then(function (object) {
          var msg = object.data["msg"];
          if (msg) flash(msg);
          var label = object.data["label"];
          if (label == '/VInicioUsuario') {
              $route.reload();
          } else {
              $location.path(label);
          }
        });};

    }]);
eventosModule.controller('VEventoUsuarioController', 
   ['$scope', '$location', '$route', '$routeParams', 'flash', 'loginService', 'usuarioService',
    function ($scope, $location, $route, $routeParams, flash, loginService, usuarioService) {
      $scope.msg = '';
      usuarioService.VEventoUsuario($routeParams.idEvento).then(function (object) {
        $scope.res = object.data;
        for (var key in object.data) {
            $scope[key] = object.data[key];
        }
        if ($scope.logout) {
            $location.path('/');
        }
      });
      $scope.VInicioUsuario1 = function() {
        $location.path('/VInicioUsuario');
      };
      $scope.AInscribirEvento0 = function(evento) {
          
        usuarioService.AInscribirEvento({"evento":((typeof evento === 'object')?JSON.stringify(evento):evento)}).then(function (object) {
          var msg = object.data["msg"];
          if (msg) flash(msg);
          var label = object.data["label"];
          if (label == '/VEventoUsuario') {
              $route.reload();
          } else {
              $location.path(label);
          }
        });};
      $scope.VAficheUsuario1 = function() {
        $location.path('/VAficheUsuario');
      };
      $scope.VCredenciales9 = function(args) {
        $location.path('/VCredenciales/'+args);
      };
      $scope.AGenerarCredencial2 = function(evento) {
          
        usuarioService.AGenerarCredencial({"evento":((typeof evento === 'object')?JSON.stringify(evento):evento)}).then(function (object) {
          var msg = object.data["msg"];
          if (msg) flash(msg);
          var label = object.data["label"];
          if (label == '/VEventoUsuario') {
              $route.reload();
          } else {
              $location.path(label);
          }
        });};
      $scope.confirmarRegistro = function(idEvento) {
        if (confirm("̣¿Está seguro de que desea inscribirse en este evento?")) {
				$scope.AInscribirEvento0(idEvento);
	    }
      };  
      $scope.ADesconectarseUsuario3 = function() {
          
        usuarioService.ADesconectarseUsuario().then(function (object) {
          var msg = object.data["msg"];
          if (msg) flash(msg);
          var label = object.data["label"];
          if (label == '/VEventoUsuario') {
              $route.reload();
          } else {
              $location.path(label);
          }
        });};
      $scope.AGenerarCertificado4 = function(evento) {
          
        usuarioService.AGenerarCertificado({"evento":((typeof evento === 'object')?JSON.stringify(evento):evento)}).then(function (object) {
          var msg = object.data["msg"];
          if (msg) flash(msg);
          var label = object.data["label"];
          if (label == '/VEventoUsuario') {
              $route.reload();
          } else {
              $location.path(label);
          }
        });};
      $scope.VCertificadoUsuario5 = function() {
        $location.path('/VCertificadoUsuario');
      };

    }]);

eventosModule.controller('VCredencialesController', 
   ['$scope', '$location', '$route', '$routeParams', 'flash', 'loginService', 'usuarioService',
    function ($scope, $location, $route, $routeParams, flash, loginService, usuarioService) {
      $scope.msg = '';
      usuarioService.VCredenciales($routeParams.idEvento).then(function (object) {
        $scope.res = object.data;
        for (var key in object.data) {
            $scope[key] = object.data[key];
        }
        if ($scope.logout) {
            $location.path('/');
        }
      });
      $scope.VEventoUsuario9 = function(args) {
        $location.path('/VEventoUsuario/'+args);
      };
      $scope.ADesconectarseUsuario9 = function() {
          
        usuarioService.ADesconectarseUsuario().then(function (object) {
          var msg = object.data["msg"];
          if (msg) flash(msg);
          var label = object.data["label"];
          if (label == '/VEventoUsuario') {
              $route.reload();
          } else {
              $location.path(label);
          }
        });};
    }]);
    
    
eventosModule.controller('VAficheUsuarioController', 
   ['$scope', '$location', '$route', 'flash', 'loginService', 'usuarioService',
    function ($scope, $location, $route, flash, loginService, usuarioService) {
      $scope.msg = '';
      usuarioService.VAficheUsuario().then(function (object) {
        $scope.res = object.data;
        for (var key in object.data) {
            $scope[key] = object.data[key];
        }
        if ($scope.logout) {
            $location.path('/');
        }
      });
      $scope.VAficheUsuario0 = function() {
        $location.path('/VAficheUsuario');
      };

    }]);
eventosModule.controller('VCertificadoUsuarioController', 
   ['$scope', '$location', '$route', 'flash', 'loginService', 'usuarioService',
    function ($scope, $location, $route, flash, loginService, usuarioService) {
      $scope.msg = '';
      usuarioService.VCertificadoUsuario().then(function (object) {
        $scope.res = object.data;
        for (var key in object.data) {
            $scope[key] = object.data[key];
        }
        if ($scope.logout) {
            $location.path('/');
        }
      });
      $scope.VEventoUsuario0 = function() {
        $location.path('/VEventoUsuario');
      };

    }]);
