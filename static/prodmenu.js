new Vue({
        el: '#prodmenu_app',
        data: {
            products: [],
            products_independant: [],
            products_garnir: [],
            products_osnova: [],
            products_soup: [],
            randomPr_indep: "",
            randomPr_garOsn: "",
            randomPr_soup: "",
            idxprev1: -1,
            idxprev2: -1,
            idxprev3: -1,
            idxprev4: -1,
        },
        created: function () {
            axios.get('/api/v1/food/prodmenu/').then((response) =>{
                this.products = response.data

                this.products_independant = response.data.filter((value, index) => value.type_id === 1);
                this.products_garnir = response.data.filter((value, index) => value.type_id === 2);
                this.products_osnova = response.data.filter((value, index) => value.type_id === 3);
                this.products_soup = response.data.filter((value, index) => value.type_id === 4);

                this.idxprev1 = Math.floor(Math.random() * this.products_independant.length);
                this.idxprev2 = Math.floor(Math.random() * this.products_garnir.length);
                this.idxprev3 = Math.floor(Math.random() * this.products_osnova.length);
                this.idxprev4 = Math.floor(Math.random() * this.products_soup.length);

                this.randomPr_indep = this.products_independant[this.idxprev1].name
                let garOsn = ""
                garOsn = this.products_garnir[this.idxprev2].name
                garOsn += " и " + this.products_osnova [this.idxprev3].name
                this.randomPr_garOsn = garOsn
                this.randomPr_soup = this.products_soup[this.idxprev4].name
            })
        },
        methods: {
            getRandomFood() {
                this.getIndepFood();
                this.getGarOsnFood();
                this.getSoupFood();
            },
            getIndepFood() {
                let idx1 = Math.floor(Math.random() * this.products_independant.length);
                while (idx1 === this.idxprev1) {
                    idx1 = Math.floor(Math.random() * this.products_independant.length);
                }
                this.idxprev1 = idx1
                this.randomPr_indep = this.products_independant[idx1].name
            },
            getGarOsnFood() {
                let garOsn = ""
                let idx2 = Math.floor(Math.random() * this.products_garnir.length);
                while (idx2 === this.idxprev2) {
                    idx2 = Math.floor(Math.random() * this.products_garnir.length);
                }
                this.idxprev2 = idx2

                garOsn = this.products_garnir[idx2].name

                let idx3 = Math.floor(Math.random() * this.products_osnova.length);
                while (idx3 === this.idxprev3) {
                    idx3 = Math.floor(Math.random() * this.products_osnova.length);
                }
                this.idxprev3 = idx3

                garOsn += " и " + this.products_osnova [idx3].name
                this.randomPr_garOsn = garOsn
            },
            getSoupFood() {
                let idx4 = Math.floor(Math.random() * this.products_soup.length);
                while (idx4 === this.idxprev4) {
                    idx4 = Math.floor(Math.random() * this.products_soup.length);
                }
                this.idxprev4 = idx4
                this.randomPr_soup = this.products_soup[idx4].name
            }
        }
    }
)
