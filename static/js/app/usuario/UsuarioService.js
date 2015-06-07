eventosModule.service('usuarioService', ['$q', '$http', function($q, $http) {

    this.AInscribirEvento = function(args) {
        if(typeof args == 'undefined') args={};
        return $http({
          url: 'usuario/AInscribirEvento',
          method: 'GET',
          params: args
        });
    //    var labels = ["/VInicioUsuario", "/VEventoUsuario", ];
    //    var res = labels[0];
    //    var deferred = $q.defer();
    //    deferred.resolve(res);
    //    return deferred.promise;
    };
    this.VInicioUsuario = function(args) {
        if(typeof args == 'undefined') args={};
        return $http({
          url: 'usuario/VInicioUsuario',
          method: 'GET',
          params: args
        });
    //    var res = {};
    //    var deferred = $q.defer();
    //    deferred.resolve(res);
    //    return deferred.promise;
    };

	this.VCredenciales = function(args) {
        if(typeof args == 'undefined') args={};
        return $http({
          url: 'usuario/VCredenciales/'+args,
          method: 'GET',
          params: args
        });
    //    var res = {};
    //    var deferred = $q.defer();
    //    deferred.resolve(res);
    //    return deferred.promise;
    };

    this.AGenerarCredencial = function(args) {
        if(typeof args == 'undefined') args={};
        return $http({
          url: 'usuario/AGenerarCredencial',
          method: 'GET',
          params: args
        });
    //    var labels = ["/VEventoUsuario", ];
    //    var res = labels[0];
    //    var deferred = $q.defer();
    //    deferred.resolve(res);
    //    return deferred.promise;
    };
    this.VEventoUsuario = function(args) {
        if(typeof args == 'undefined') args={};
        return $http({
          url: 'usuario/VEventoUsuario/'+args,
          method: 'GET',
          params: args
        });
    //    var res = {};
    //    var deferred = $q.defer();
    //    deferred.resolve(res);
    //    return deferred.promise;
    };

    this.ADesconectarseUsuario = function(args) {
        if(typeof args == 'undefined') args={};
        return $http({
          url: 'usuario/ADesconectarseUsuario',
          method: 'GET',
          params: args
        });
    //    var labels = ["/VPortada", ];
    //    var res = labels[0];
    //    var deferred = $q.defer();
    //    deferred.resolve(res);
    //    return deferred.promise;
    };
    this.AGenerarCertificado = function(args) {
        if(typeof args == 'undefined') args={};
        return $http({
          url: 'usuario/AGenerarCertificado',
          method: 'GET',
          params: args
        });
    //    var labels = ["/VEventoUsuario", ];
    //    var res = labels[0];
    //    var deferred = $q.defer();
    //    deferred.resolve(res);
    //    return deferred.promise;
    };
    this.VAficheUsuario = function(args) {
        if(typeof args == 'undefined') args={};
        return $http({
          url: 'usuario/VAficheUsuario/'+args,
          method: 'GET',
          params: args
        });
    //    var res = {};
    //    var deferred = $q.defer();
    //    deferred.resolve(res);
    //    return deferred.promise;
    };

    this.VCertificadoUsuario = function(args) {
        if(typeof args == 'undefined') args={};
        return $http({
          url: 'usuario/VCertificadoUsuario/'+args,
          method: 'GET',
          params: args
        });
    //    var res = {};
    //    var deferred = $q.defer();
    //    deferred.resolve(res);
    //    return deferred.promise;
    };

}]);
