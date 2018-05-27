angular.module('AppChat').controller('HomeController', ['$http', '$log', '$rootScope', '$scope', '$location',
   function($http, $log, $scope, $rootScope, $location) {
        var thisCtrl = this;
        this.groupChatList = [];
        this.counter  = 2;
        var uid = $scope.user.uid;



        this.loadGroupChats = function(){
            //console.log($rootScope.uid)
            //console.log("test");
            if (uid%1!==0)
                $location.url('/login');

            var url = "http://127.0.0.1:5000/MessagingApp_DB/users/" + uid + "/groupchats/";

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
        this.loadGroupChats();

        $scope.goToChat = function(gid, gname){
            $scope.gid = gid;
            console.log("gname from home is: " + gname);
            $scope.gname = gname;

            $location.url('/chat');

        };

   }]);