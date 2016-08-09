"use strict";


angular.module('app.bill', ['ui.router'])
.config(function ($stateProvider) {

    $stateProvider
        .state('app.bill', {
            url: '/bill',
            data: {
                title: 'Blank'
            },
            views: {
                "content@app": {
                    templateUrl: 'app/bill/views/bill.html',
                    controller: 'BillController'
                }
            }
        })
});
