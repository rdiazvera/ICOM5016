angular.module('AppChat').controller('ChatController', ['$http', '$log', '$scope', '$rootScope', '$location',
    function($http, $log, $scope, $rootScope, $location) {
        var thisCtrl = this;
        this.messageList = [];
        this.counter  = 2;
        this.newText = "";
        this.search = "";
        var groupName = $scope.gname;
        var gid = $scope.gid;
        var uid = $scope.user.uid;
        var mid = $scope.mid;




        this.loadMessages = function(){
            console.log("GID IS: " + gid);
            console.log("UID IS: " + uid);
            console.log("Gname is: " + groupName);
            var url = "http://127.0.0.1:5000/MessagingApp_DB/groupchats/" + gid + "/messages/";

            $http.get(url).then(
                function(response){
                    console.log("response: " + JSON.stringify(response));
                    thisCtrl.messageList = response.data.Messages;

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

                $log.error("Message Loaded: ", JSON.stringify(thisCtrl.messageList));
        };

        this.postMsg = function(){
            var msg = thisCtrl.newText;

            var url = "http://127.0.0.1:5000/MessagingApp_DB/groupchats/" + gid + "/messages/";
            var data = JSON.stringify({uid: uid, text: msg});

            $http.post(url, data).then(

                function(response){
                    console.log(data);
                    console.log("response: " + JSON.stringify(response));
                    thisCtrl.messageList = response.data.Messages;
                    this.loadMessages();
                },
                function(response){
                    console.log("3");
                    console.log(response.status);
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
                //$log.error("Message Loaded: ", JSON.stringify(thisCtrl.messageList));
//            thisCtrl.messageList.unshift({"mid": nextId, "text" : msg, "username" : username, "Name" : Name,
//            "like" : 0, "dislike" : 0, "date_created": "just now"});
             thisCtrl.newText = "";
        };

        this.likeMsg = function(mid){
            var url = "http://127.0.0.1:5000/MessagingApp_DB/messages/" + mid + "/likes/count/";
            console.log("gid is: " + $scope.gid);
            var data = JSON.stringify({uid: uid, mid: mid, type: "like", gid: $scope.gid});
            $http.post(url, data).then(

                function(response){
                    console.log(data);
                    console.log("response: " + JSON.stringify(response));
                    thisCtrl.messageList = response.data.Messages;
                },
                function(response){
                    console.log("3");
                    console.log(response.status);
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
                        alert("You Already Reacted.");
                    }
                });
                //$log.error("Message Loaded: ", JSON.stringify(thisCtrl.messageList));
        };

        this.dislikeMsg = function(mid){

            var url = "http://127.0.0.1:5000/MessagingApp_DB/messages/" + mid + "/dislikes/count/";
            //"http://127.0.0.1:5000/MessagingApp_DB/messages/"+"<int:+" data[1] + ">/dislikes/count/";
            var data = JSON.stringify({uid: uid, mid: mid, type: "dislike", gid: $scope.gid})
            $http.post(url, data).then(

                function(response){
                    console.log(data);
                    console.log("response: " + JSON.stringify(response));
                    thisCtrl.messageList = response.data.Messages;
                },
                function(response){
                    console.log("3");
                    console.log(response.status);
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
                        alert("You Already Reacted.");
                    }

                });
                //$log.error("Message Loaded: ", JSON.stringify(thisCtrl.messageList));
        };

        this.replyMsg = function(){
            alert("The \"Reply\" button is under construction.");
        };

        this.userLike = function(mid){

            var url = "http://127.0.0.1:5000/MessagingApp_DB/messages/" + mid + "/likes/users/";
            $http.get(url).then(
                function(response){
                    console.log(mid);
                    console.log("response: " + JSON.stringify(response));

                    var array = [];
                    for (var x = 0; x< response.data.Users.length; x++){
                        console.log(response.data.Users[x].username);
                        array.push(response.data.Users[x].username);
                    }
                    console.log(array);
                    alert("Liked By: \n" + array.join("\n"));
                },
                function(response){
                    console.log("3");
                    console.log(response.status);
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
                //$log.error("Message Loaded: ", JSON.stringify(thisCtrl.messageList));

        };

       this.userDislike = function(mid){

            var url = "http://127.0.0.1:5000/MessagingApp_DB/messages/" + mid + "/dislikes/users/";
            $http.get(url).then(
                function(response){
                    console.log(mid);
                    console.log("response: " + JSON.stringify(response));

                    var array = [];
                    for (var x = 0; x< response.data.Users.length; x++){
                        console.log(response.data.Users[x].username);
                        array.push(response.data.Users[x].username);
                    }
                    console.log(array);
                    alert("Disliked By: \n" + array.join("\n"));
                },
                function(response){
                    console.log("3");
                    console.log(response.status);
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
                //$log.error("Message Loaded: ", JSON.stringify(thisCtrl.messageList));

        };

        this.postReplyMsg = function(text, replied_id){
            var msg = thisCtrl.newReplyText;
            // Need to figure out who I am

            var url = "http://127.0.0.1:5000/MessagingApp_DB/groupchats/" + gid + "/messages/reply";
            var data = JSON.stringify({uid: uid, text: "\"RE: " +text + "\" " + msg, mid: replied_id});

            $http.post(url, data).then(

                function(response){
                    console.log(data);
                    console.log("response: " + JSON.stringify(response));
                    thisCtrl.messageList = thisCtrl.messageList = response.data.Messages;
                },
                function(response){
                    console.log("3");
                    console.log(response.status);
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
                //$log.error("Message Loaded: ", JSON.stringify(thisCtrl.messageList));
//            thisCtrl.messageList.unshift({"mid": nextId, "text" : msg, "username" : username, "Name" : Name,
//            "like" : 0, "dislike" : 0, "date_created": "just now"});
             thisCtrl.newReplyText = "";
        };

         $scope.goToHome = function(){
             $scope.gid = 0;
             $location.url('/home');

        };

        this.loadMessages();
}]);
