angular.module('AppChat').controller('ChatController', ['$http', '$log', '$scope',
    function($http, $log, $scope) {
        /* TESTING FUNCTION
        $scope.example = {};

        $scope.getData = function(){
            $http.get("appjs/example.json").then(
                function(response){
                    var messageData = response.data.Messages;
                    $scope.example = messageData[1].text;
                }
            )
        };
        $scope.getData();
        */

        var thisCtrl = this;

        this.messageList = [];
        this.counter  = 2;
        this.newText = "";

        this.loadMessages = function(){

            var url = "http://127.0.0.1:5000/MessagingApp_DB/messages/";

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
            // Need to figure out who I am
            var username = "EL_FELI_1924 ";
            var Name = "Felipe Santiago"
            var nextId = thisCtrl.counter++;
            thisCtrl.messageList.unshift({"mid": nextId, "text" : msg, "username" : username, "Name" : Name,
            "like" : 0, "dislike" : 0, "date_created": "just now"});
            thisCtrl.newText = "";
        };

        this.loadMessages();
}]);
