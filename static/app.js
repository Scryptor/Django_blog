new Vue({
        el: '#aboutme_app',
        data: {
            me: []
        },
        created: function () {
            axios.get('/api/v1/about/').then((response) => {
                this.me = response.data
            })
        }
    }
)
