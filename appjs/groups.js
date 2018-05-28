angular.module('AppChat').controller('GroupController', ['$http', '$log', '$rootScope', '$scope', '$location',
   function($http, $log, $scope, $rootScope, $location) {
        var thisCtrl = this;
        var uid = $scope.user.uid;
        this.groupChatList = [];

            this.loadGroupChats = function(){
            console.log("en el controller");
            if (uid%1!==0)
                $location.url('/login');

            var url = "http://127.0.0.1:5000/MessagingApp_DB/GroupChats/" + uid + '/available/';

            $http.get(url).then(
                function(response){
                    console.log("response: " + JSON.stringify(response));
                    console.log(response.data)
                    thisCtrl.groupChatList = response.data.GroupChats;
                },
                function(response){
                    var status = response.status;
                    if (status == 0){
                        alert("No internet connection.");
                    }
                    else if (status == 401){
                        alert("Session Expired.");
                    }
                    else if (status == 403){
                        alert("Not authorized.");
                    }
                    else if (status == 404){
                        alert("Not Found.");
                    }
                    else {
                        alert("Internal system error.");
                    }
                });

                $log.error("Message Loaded: ", JSON.stringify(thisCtrl.groupChatList));
        };

         $scope.goToHome = function(){
             console.log("hola")
             $location.url('/home');

        };

        this.loadGroupChats();


   }]);