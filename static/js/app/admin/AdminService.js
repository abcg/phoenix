eventosModule.service('adminService', ['$q', '$http', function($q, $http) {

    this.VInicioAdministrador = function(args) {
        if(typeof args == 'undefined') args={};
        return $http({
          url: 'admin/VInicioAdministrador',
          method: 'GET',
          params: args
        });
    //    var res = {};
    //    var deferred = $q.defer();
    //    deferred.resolve(res);
    //    return deferred.promise;
    };

    this.ARegistrarEvento = function(registroEventoForm) {
        return  $http({
          url: "admin/ARegistrarEvento",
          data: registroEventoForm,
          method: 'POST',
        });
    //    var labels = ["/VEvento", "/VRegistroEvento", ];
    //    var res = labels[0];
    //    var deferred = $q.defer();
    //    deferred.resolve(res);
    //    return deferred.promise;
    };

    this.AModificarEvento = function(modificacionEventoForm) {
        return  $http({
          url: "admin/AModificarEvento",
          data: modificacionEventoForm,
          method: 'POST',
        });
    //    var labels = ["/VEvento", "/VModificarEvento", ];
    //    var res = labels[0];
    //    var deferred = $q.defer();
    //    deferred.resolve(res);
    //    return deferred.promise;
    };

    this.VEvento = function(args) {
        if(typeof args == 'undefined') args={};
        return $http({
          url: 'admin/VEvento',
          method: 'GET',
          params: args
        });
    //    var res = {};
    //    var deferred = $q.defer();
    //    deferred.resolve(res);
    //    return deferred.promise;
    };

    this.AEliminarEvento = function(args) {
        if(typeof args == 'undefined') args={};
        return $http({
          url: 'admin/AEliminarEvento',
          method: 'GET',
          params: args
        });
    //    var labels = ["/VInicioAdministrador", "/VEvento", ];
    //    var res = labels[0];
    //    var deferred = $q.defer();
    //    deferred.resolve(res);
    //    return deferred.promise;
    };
    this.AGuardarAsistencia = function(args) {
        if(typeof args == 'undefined') args={};
        return $http({
          url: 'admin/AGuardarAsistencia',
          method: 'GET',
          params: args
        });
    //    var labels = ["/VParticipantes", "/VParticipantes", ];
    //    var res = labels[0];
    //    var deferred = $q.defer();
    //    deferred.resolve(res);
    //    return deferred.promise;
    };
    this.ADesconectarse = function(args) {
        if(typeof args == 'undefined') args={};
        return $http({
          url: 'admin/ADesconectarse',
          method: 'GET',
          params: args
        });
    //    var labels = ["/VPortada", ];
    //    var res = labels[0];
    //    var deferred = $q.defer();
    //    deferred.resolve(res);
    //    return deferred.promise;
    };
    this.VRegistroEvento = function(args) {
        if(typeof args == 'undefined') args={};
        return $http({
          url: 'admin/VRegistroEvento',
          method: 'GET',
          params: args
        });
    //    var res = {};
    //    var deferred = $q.defer();
    //    deferred.resolve(res);
    //    return deferred.promise;
    };

    this.VAfiche = function(args) {
        if(typeof args == 'undefined') args={};
        return $http({
          url: 'admin/VAfiche',
          method: 'GET',
          params: args
        });
    //    var res = {};
    //    var deferred = $q.defer();
    //    deferred.resolve(res);
    //    return deferred.promise;
    };

    this.VParticipantes = function(args) {
        if(typeof args == 'undefined') args={};
        return $http({
          url: 'admin/VParticipantes',
          method: 'GET',
          params: args
        });
    //    var res = {};
    //    var deferred = $q.defer();
    //    deferred.resolve(res);
    //    return deferred.promise;
    };

    this.VModificarEvento = function(args) {
        if(typeof args == 'undefined') args={};
        return $http({
          url: 'admin/VModificarEvento',
          method: 'GET',
          params: args
        });
    //    var res = {};
    //    var deferred = $q.defer();
    //    deferred.resolve(res);
    //    return deferred.promise;
    };

}]);