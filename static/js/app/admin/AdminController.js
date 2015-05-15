eventosModule.config(function ($routeProvider) {
    $routeProvider.when('/VInicioAdministrador', {
                controller: 'VInicioAdministradorController',
                templateUrl: 'app/admin/VInicioAdministrador.html'
            }).when('/VEvento/:idEvento', {
                controller: 'VEventoController',
                templateUrl: 'app/admin/VEvento.html'
            }).when('/VRegistroEvento', {
                controller: 'VRegistroEventoController',
                templateUrl: 'app/admin/VRegistroEvento.html'
            }).when('/VAfiche', {
                controller: 'VAficheController',
                templateUrl: 'app/admin/VAfiche.html'
            }).when('/VParticipantes', {
                controller: 'VParticipantesController',
                templateUrl: 'app/admin/VParticipantes.html'
            }).when('/VModificarEvento', {
                controller: 'VModificarEventoController',
                templateUrl: 'app/admin/VModificarEvento.html'
            });
});

eventosModule.controller('VInicioAdministradorController', 
   ['$scope', '$location', '$route', 'flash', 'adminService', 'loginService',
    function ($scope, $location, $route, flash, adminService, loginService) {
      $scope.msg = '';
      adminService.VInicioAdministrador().then(function (object) {
        $scope.res = object.data;
        for (var key in object.data) {
            $scope[key] = object.data[key];
        }
        if ($scope.logout) {
            $location.path('/');
        }
      });
      $scope.VRegistroEvento0 = function() {
        $location.path('/VRegistroEvento');
      };
      $scope.VEvento1 = function(args) {
        $location.path('/VEvento/'+args);
      };
      $scope.ADesconectarse2 = function() {
          
        adminService.ADesconectarse().then(function (object) {
          var msg = object.data["msg"];
          if (msg) flash(msg);
          var label = object.data["label"];
          if (label == '/VInicioAdministrador') {
              $route.reload();
          } else {
              $location.path(label);
          }
        });};

    }]);
eventosModule.controller('VEventoController', 
   ['$scope', '$location', '$route', '$routeParams', 'flash', 'adminService', 'loginService',
    function ($scope, $location, $route, $routeParams, flash, adminService, loginService) {
      $scope.msg = '';
      adminService.VEvento($routeParams.idEvento).then(function (object) {
        $scope.res = object.data;
        for (var key in object.data) {
            $scope[key] = object.data[key];
        }
        if ($scope.logout) {
            $location.path('/');
        }
      });
      $scope.VAfiche0 = function() {
        $location.path('/VAfiche');
      };
      $scope.VModificarEvento1 = function() {
        $location.path('/VModificarEvento');
      };
      $scope.VParticipantes2 = function() {
        $location.path('/VParticipantes');
      };
      $scope.VInicioAdministrador1 = function() {
        $location.path('/VInicioAdministrador');
      };
      $scope.AEliminarEvento3 = function(evento) {
          
        adminService.AEliminarEvento({"evento":((typeof evento === 'object')?JSON.stringify(evento):evento)}).then(function (object) {
          var msg = object.data["msg"];
          if (msg) flash(msg);
          var label = object.data["label"];
          if (label == '/VEvento') {
              $route.reload();
          } else {
              $location.path(label);
          }
        });};
      $scope.ADesconectarse4 = function() {
          
        adminService.ADesconectarse().then(function (object) {
          var msg = object.data["msg"];
          if (msg) flash(msg);
          var label = object.data["label"];
          if (label == '/VEvento') {
              $route.reload();
          } else {
              $location.path(label);
          }
        });};

    }]);
eventosModule.controller('VRegistroEventoController', 
   ['$scope', '$location', '$route', 'flash', 'adminService', 'loginService',
    function ($scope, $location, $route, flash, adminService, loginService) {
      $scope.msg = '';
      $scope.registroEventoForm = {};

      adminService.VRegistroEvento().then(function (object) {
        $scope.res = object.data;
        for (var key in object.data) {
            $scope[key] = object.data[key];
        }
        if ($scope.logout) {
            $location.path('/');
        }
      });
      $scope.VInicioAdministrador0 = function() {
        $location.path('/VInicioAdministrador');
      };
      $scope.ADesconectarse2 = function() {
          
        adminService.ADesconectarse().then(function (object) {
          var msg = object.data["msg"];
          if (msg) flash(msg);
          var label = object.data["label"];
          if (label == '/VRegistroEvento') {
              $route.reload();
          } else {
              $location.path(label);
          }
        });};

      $scope.registroEventoFormSubmitted = false;
      $scope.ARegistrarEvento1 = function(isValid) {
        $scope.registroEventoFormSubmitted = true;
        if (isValid) {
          
          adminService.ARegistrarEvento($scope.registroEventoForm).then(function (object) {
              var msg = object.data["msg"];
              if (msg) flash(msg);
              var label = object.data["label"];
              if (label == '/VRegistroEvento') {
                  $route.reload();
              } else {
                  $location.path(label);
              }
          });
        }
      };

    }]);
eventosModule.controller('VAficheController', 
   ['$scope', '$location', '$route', 'flash', 'adminService', 'loginService',
    function ($scope, $location, $route, flash, adminService, loginService) {
      $scope.msg = '';
      adminService.VAfiche().then(function (object) {
        $scope.res = object.data;
        for (var key in object.data) {
            $scope[key] = object.data[key];
        }
        if ($scope.logout) {
            $location.path('/');
        }
      });
    }]);
eventosModule.controller('VParticipantesController', 
   ['$scope', '$location', '$route', 'flash', 'adminService', 'loginService',
    function ($scope, $location, $route, flash, adminService, loginService) {
      $scope.msg = '';
      adminService.VParticipantes().then(function (object) {
        $scope.res = object.data;
        for (var key in object.data) {
            $scope[key] = object.data[key];
        }
        if ($scope.logout) {
            $location.path('/');
        }
      });
      $scope.VEvento0 = function() {
        $location.path('/VEvento');
      };
      $scope.AGuardarAsistencia1 = function(participantes) {
          
        adminService.AGuardarAsistencia({"participantes":((typeof participantes === 'object')?JSON.stringify(participantes):participantes)}).then(function (object) {
          var msg = object.data["msg"];
          if (msg) flash(msg);
          var label = object.data["label"];
          if (label == '/VParticipantes') {
              $route.reload();
          } else {
              $location.path(label);
          }
        });};
      $scope.ADesconectarse2 = function() {
          
        adminService.ADesconectarse().then(function (object) {
          var msg = object.data["msg"];
          if (msg) flash(msg);
          var label = object.data["label"];
          if (label == '/VParticipantes') {
              $route.reload();
          } else {
              $location.path(label);
          }
        });};

    }]);
eventosModule.controller('VModificarEventoController', 
   ['$scope', '$location', '$route', 'flash', 'adminService', 'loginService',
    function ($scope, $location, $route, flash, adminService, loginService) {
      $scope.msg = '';
      $scope.modificacionEventoForm = {};

      adminService.VModificarEvento().then(function (object) {
        $scope.res = object.data;
        for (var key in object.data) {
            $scope[key] = object.data[key];
        }
        if ($scope.logout) {
            $location.path('/');
        }
      });
      $scope.VEvento1 = function() {
        $location.path('/VEvento');
      };
      $scope.ADesconectarse2 = function() {
          
        adminService.ADesconectarse().then(function (object) {
          var msg = object.data["msg"];
          if (msg) flash(msg);
          var label = object.data["label"];
          if (label == '/VModificarEvento') {
              $route.reload();
          } else {
              $location.path(label);
          }
        });};

      $scope.modificacionEventoFormSubmitted = false;
      $scope.AModificarEvento0 = function(isValid) {
        $scope.modificacionEventoFormSubmitted = true;
        if (isValid) {
          
          adminService.AModificarEvento($scope.modificacionEventoForm).then(function (object) {
              var msg = object.data["msg"];
              if (msg) flash(msg);
              var label = object.data["label"];
              if (label == '/VModificarEvento') {
                  $route.reload();
              } else {
                  $location.path(label);
              }
          });
        }
      };

    }]);
