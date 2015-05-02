eventosModule.service('loginService', ['$q', '$http', function($q, $http) {

    this.AIdentificar = function(args) {
        if(typeof args == 'undefined') args={};
        return $http({
          url: 'login/AIdentificar',
          method: 'GET',
          params: args
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

}]);