new Vue({
        el: '#blog_app',
        data: {
            blogs: [],
            nextpage: null,
            prevpage: null,
            currpage: 1,
        },
        created: function () {
            let search_text = ''
            let urlParams = new URLSearchParams(window.location.search);
            if (urlParams.has('query'))
                search_text = urlParams.get('query');
            axios.get('/api/v1/posts/?ordering=-creation_date&search=' + search_text).then((response) => {
                this.blogs = response.data.results
                this.nextpage = response.data.next
                this.prevpage = response.data.previous
            })
        },
        methods: {
            goToNextPage() {
                this.currpage++
                axios.get(this.nextpage).then((response) => {
                    this.blogs = response.data.results
                    this.nextpage = response.data.next
                    this.prevpage = response.data.previous
                })
            },
            goToPrevPage() {
                this.currpage--
                axios.get(this.prevpage).then((response) => {
                    this.blogs = response.data.results
                    this.nextpage = response.data.next
                    this.prevpage = response.data.previous
                })
            },
        }
    }
)


Vue.filter('truncate', function (text, length, clamp) {
    clamp = clamp || '...';
    var node = document.createElement('div');
    node.innerHTML = text;
    var content = node.textContent;
    return content.length > length ? content.slice(0, length) + clamp : content
});


Vue.filter('formatDate', function (value) {
    if (value) {
        let dtime = new Date(value);
        return dtime.toLocaleString()
    }
});