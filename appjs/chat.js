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

            $http.get("appjs/example.json").then(
                function(response){
                    var messageData = response.data.Messages;
                    for(var i = 0; i < 5; i++){
                        thisCtrl.messageList.push({"id": messageData[1].mid, "text": messageData[i].text, "author" : messageData[i].uid, "like" : 1, "nolike" : 1});
                    }

                    $scope.example = messageData[1].text;
                }
            );

            /*
            // Get the messages from the server through the rest api
            thisCtrl.messageList.push({"id": 2, "text": "Hola Mi Amigo", "author" : "Bob",
            "like" : 4, "nolike" : 1});
            thisCtrl.messageList.push({"id": 3, "text": "Hello World", "author": "Joe",
                "like" : 11, "nolike" : 12});
            */

            $log.error("Message Loaded: ", JSON.stringify(thisCtrl.messageList));
        };

        this.postMsg = function(){
            var msg = thisCtrl.newText;
            // Need to figure out who I am
            var author = "Me";
            var nextId = thisCtrl.counter++;
            thisCtrl.messageList.unshift({"id": nextId, "text" : msg, "author" : author, "like" : 0, "nolike" : 0});
            thisCtrl.newText = "";
        };

        this.loadMessages();
}]);
