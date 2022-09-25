new Vue({
        el: '#blog_app',
        data: {
            blogs: []
        },
        created: function () {
            const vm = this
            axios.get('/api/v1/posts/?ordering=-creation_date').then(function (response) {
                vm.blogs = response.data
            })
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