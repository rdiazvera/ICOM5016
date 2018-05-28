angular.module('AppChat').controller('HomeController', ['$http', '$log', '$rootScope', '$scope', '$location',
   function($http, $log, $scope, $rootScope, $location) {
        var thisCtrl = this;
        this.groupChatList = [];
        this.availableGroupChatList = [];
        this.counter  = 2;
        var uid = $scope.user.uid;
        this.newGroupName = "";

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
            $scope.gname = gname;
            $location.url('/chat');

        };

        $scope.goToAvailableGroupChats = function(){
         $location.url('/groups');
         };

         $scope.createGroupChat = function(uid){
            console.log("New Group Chat Name: " + thisCtrl.newGroupName);
            console.log("Owner ID: " + $scope.user.uid);
            var url = "http://127.0.0.1:5000/MessagingApp_DB/GroupChats/" + $scope.user.uid + "/available/";
            var data = {gname: thisCtrl.newGroupName};

            $http.post(url, data).then(
                function(response){
                    console.log("response: " + JSON.stringify(response));
                    console.log(response.data);
                    alert("Group Chat Created Successfully!");
                    thisCtrl.groupChatList = response.data.GroupChats;
                    this.loadGroupChats();

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

         this.loadGroupChats();

        };


         this.loadAvailableGroupChats = function(){
            if (uid%1!==0)
                $location.url('/login');

            var url = "http://127.0.0.1:5000/MessagingApp_DB/GroupChats/" + uid + "/available";

            $http.get(url).then(
                function(response){
                    console.log("response: " + JSON.stringify(response));
                    console.log(response.data)
                    thisCtrl.availableGroupChatList = response.data.GroupChats;
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
         this.loadAvailableGroupChats();

      $scope.joinChat = function(gid) {
          var url = "http://127.0.0.1:5000/MessagingApp_DB/groupchats/" + gid + "/users/";
          var data = {uid: uid }
          $http.post(url, data).then(
                function(response){
                    alert("group joined successfully");
                    $location.url('/home');
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

   }]);