eventosModule.service('loginService', ['$q', '$http', function($q, $http) {

    this.AIdentificar = function(loginForm) {
        return  $http({
          url: "login/AIdentificar",
          data: loginForm,
          method: 'POST',
        });
    //    var labels = ["/VInicioAdministrador", "/VInicioUsuario", "/VPortada", ];
    //    var res = labels[0];
    //    var deferred = $q.defer();
    //    deferred.resolve(res);
    //    return deferred.promise;
    };

    this.VPortada = function(args) {
        if(typeof args == 'undefined') args={};
        return $http({
          url: 'login/VPortada',
          method: 'GET',
          params: args
        });
    //    var res = {};
    //    var deferred = $q.defer();
    //    deferred.resolve(res);
    //    return deferred.promise;
    };

    this.VRegistroUsuario = function(args) {
        if(typeof args == 'undefined') args={};
        return $http({
          url: 'login/VRegistroUsuario',
          method: 'GET',
          params: args
        });
    //    var res = {};
    //    var deferred = $q.defer();
    //    deferred.resolve(res);
    //    return deferred.promise;
    };

    this.ARegistrarUsuario = function(registroUsuarioForm) {
        return  $http({
          url: "login/ARegistrarUsuario",
          data: registroUsuarioForm,
          method: 'POST',
        });
    //    var labels = ["/VPortada", "/VRegistroUsuario", ];
    //    var res = labels[0];
    //    var deferred = $q.defer();
    //    deferred.resolve(res);
    //    return deferred.promise;
    };

}]);