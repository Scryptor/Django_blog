new Vue({
        el: '#aboutme_app',
        data: {
            me: []
        },
        created: function () {
            const vm = this
            axios.get('/api/v1/about/').then(function (response) {
                vm.me = response.data
            })
        }
    }
)
