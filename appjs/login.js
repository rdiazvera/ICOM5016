

angular.module('AppChat').controller('LoginController', ['$http', '$log', '$scope', '$rootScope', '$location',
   function($http, $log, $scope, $rootScope, $location) {
   $rootScope.user = [];
   $rootScope.gid = 0;
   $rootScope.gname = "";

   var thisCtrl = this;
   this.loginUsername = "";
   this.loginPassword = "";
   this.registerEmail = "";
   this.registerPassword = "";
   this.registerPhone = "";
   this.registerFirstName = "";
   this.registerLastName = "";
   this.registerUsername = "";

            this.LogIn = function(){
//            var msg = thisCtrl.newText;
            console.log(thisCtrl.loginUsername);
            console.log(thisCtrl.loginPassword);

            var url = "http://127.0.0.1:5000/MessagingApp_DB/users/login/";
            var data = JSON.stringify({username: thisCtrl.loginUsername, password: thisCtrl.loginPassword});

            $http.post(url, data).then(

                function(response){
                    //console.log(data);
                    //console.log("response: " + JSON.stringify(response));
                    console.log("print del primer response");
                    $rootScope.uid = response.data.Users;
                    console.log($rootScope.uid);
                    console.log("en el response");
                    $rootScope.user = response.data.Users;
                    console.log($rootScope.user.uid);
                    console.log($rootScope.user.email);
                    console.log($rootScope.user.phone);
                    $location.url('/home');


                },
                function(response){
                    if (status == 0){
                        alert("Invalid username or password");
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

        };

            this.Register = function(){

            var url = "http://127.0.0.1:5000/MessagingApp_DB/users/register/";
            var data = JSON.stringify({username: thisCtrl.registerUsername, password: thisCtrl.registerPassword,
            first_name: thisCtrl.registerFirstName, last_name: thisCtrl.registerLastName, email: thisCtrl.registerEmail,
            phone: thisCtrl.registerPhone});

            $http.post(url, data).then(

                function(response){
                    alert("User Registered Successfully");
                    location.reload();

                },
                function(response){
                    if (status == 0){
                        alert("Invalid or empty field(s)");
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

        };

}]);

