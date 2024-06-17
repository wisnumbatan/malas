import uuid

restaurants = [
    {
        "id": "rqdv5juczeskfw1e867",
        "name": "Sate Khas Senayan",
        "description": "Restoran yang menyajikan berbagai macam sate khas Indonesia dengan cita rasa autentik.",
        "pictureId": "https://www.centralparkjakarta.com/wp-content/uploads/2017/11/sate-khas-senayan-photo.jpg",
        "city": "Jakarta",
        "rating": 4.5
    },
    {
        "id": "s1knt6za9kkfw1e867",
        "name": "Bebek Tepi Sawah",
        "description": "Restoran yang terkenal dengan hidangan bebek goreng dan suasana khas pedesaan Bali.",
        "pictureId": "https://tse4.mm.bing.net/th?id=OIP.we148eEHaNmEnPLLc1W7PgHaE6&pid=Api&P=0&h=180",
        "city": "Bali",
        "rating": 4.7
    },
    {
        "id": "w9pga3s2tubfw1e867",
        "name": "Bakmi GM",
        "description": "Restoran terkenal dengan berbagai macam bakmi yang lezat dan harga terjangkau.",
        "pictureId": "https://tse1.mm.bing.net/th?id=OIP.YmRPnM95xRYjkP5_yIEuyAHaFj&pid=Api&P=0&h=180",
        "city": "Jakarta",
        "rating": 4.3
    },
    {
        "id": "udwgdjse2wpfw1e867",
        "name": "Nasi Uduk Ibu Sum",
        "description": "Nasi uduk legendaris dengan sambal yang pedas dan lezat.",
        "pictureId": "https://tse1.mm.bing.net/th?id=OIP.RaA56Xl2m5xhbptaDqm0ewHaFi&pid=Api&P=0&h=180",
        "city": "Jakarta",
        "rating": 4.6
    },
    {
        "id": "uewifjw6w0jfw1e867",
        "name": "Warung Lela",
        "description": "Warung makan yang terkenal dengan mie ayamnya yang nikmat.",
        "pictureId": "https://tse2.mm.bing.net/th?id=OIP.6pOzk7fS9zEWLh-JNn1GCAHaEK&pid=Api&P=0&h=180",
        "city": "Bandung",
        "rating": 4.4
    },
    {
        "id": "un76djsir7rfw1e867",
        "name": "Mie Ayam Tumini",
        "description": "Mie ayam dengan porsi besar dan cita rasa yang khas.",
        "pictureId": "https://tse2.mm.bing.net/th?id=OIP.-ZfRS8VsFfJQ1gXsgDB6MAHaE7&pid=Api&P=0&h=180",
        "city": "Yogyakarta",
        "rating": 4.8
    },
    {
        "id": "s2jz3kdj92kfw1e867",
        "name": "Soto Betawi Haji Husein",
        "description": "Soto Betawi dengan kuah santan yang gurih dan daging yang empuk.",
        "pictureId": "https://tse1.mm.bing.net/th?id=OIP.Sp6MxWz4QBf6Yg8uNANCjwHaEZ&pid=Api&P=0&h=180",
        "city": "Jakarta",
        "rating": 4.5
    },
    {
        "id": "9jdm2kd92j2fw1e867",
        "name": "Ayam Bakar Wong Solo",
        "description": "Ayam bakar dengan bumbu khas Solo yang meresap hingga ke tulang.",
        "pictureId": "https://tse1.mm.bing.net/th?id=OIP.GxyrdpkWO2NnGD8sRDkZrAHaFj&pid=Api&P=0&h=180",
        "city": "Solo",
        "rating": 4.6
    },
    {
        "id": "f3jd8kdj83kf3w1e867",
        "name": "Pempek Pak Raden",
        "description": "Pempek Palembang asli dengan kuah cuko yang kental dan pedas.",
        "pictureId": "https://tse1.mm.bing.net/th?id=OIP.BIDbT7vfmlfiAVLg57ejIgHaFb&pid=Api&P=0&h=180",
        "city": "Palembang",
        "rating": 4.7
    },
    {
        "id": "f8kdk3j82kf8w1e867",
        "name": "Gudeg Yu Djum",
        "description": "Gudeg asli Yogyakarta dengan cita rasa manis dan gurih yang khas.",
        "pictureId": "https://tse3.mm.bing.net/th?id=OIP.SimA76WBMTCvbJzUPhMb7AHaE8&pid=Api&P=0&h=180",
        "city": "Yogyakarta",
        "rating": 4.9
    }
     {
        "id": "f4kdk3j82kf8w1e821",
        "name": "Ayam Goreng Suharti",
        "description": "Ayam goreng dengan bumbu kremes yang renyah dan lezat.",
        "pictureId": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS54iDgi9s9EpMRpb5Y8Ofrd2JR9qfi7bZ7VA&s",
        "city": "Yogyakarta",
        "rating": 4.5
    },
    {
        "id": "f2bdk3j82kf8w1e867",
        "name": "Bubur Ayam Barito",
        "description": "Bubur ayam dengan topping melimpah dan cita rasa gurih.",
        "pictureId": "https://manual.co.id/wp-content/uploads/2014/06/Bubur-Ayam-Barito-Street-Food_Barito-1.jpg",
        "city": "Jakarta",
        "rating": 4.4
    },
    {
        "id": "f8kdk4h82kf8w1e867",
        "name": "Sop Buntut Cut Meutia",
        "description": "Sop buntut dengan kuah yang kaya rasa dan daging yang empuk.",
        "pictureId": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTY9F8fxZ0sAGrlzgNMvBFEOP7LuUNa2u9JVQ&s",
        "city": "Jakarta",
        "rating": 4.6
    },
    {
        "id": "a2kdk3j82kf8w1e867",
        "name": "Nasi Campur Bali Men Weti",
        "description": "Nasi campur Bali dengan beragam lauk yang nikmat.",
        "pictureId": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSLNBQQUc8aMgcyBnIUpYer_WjJHWG_o0Kaug&s",
        "city": "Bali",
        "rating": 4.7
    },
    {
        "id": "o9kdk3j82kf8w1e867",
        "name": "Gado-Gado Boplo",
        "description": "Gado-gado dengan bumbu kacang yang kental dan lezat.",
        "pictureId": "https://d2dzi65yjecjnt.cloudfront.net/357959.jpg",
        "city": "Jakarta",
        "rating": 4.5
    },
    {
        "id": "f8kdk3j82kf8w1c917",
        "name": "Lontong Balap Garuda Pak Gendut",
        "description": "Lontong balap dengan kuah yang gurih dan tahu yang lembut.",
        "pictureId": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRYVcGVwbY6h1LCScIzk7MXBpAg95J6ADWA3Q&s",
        "city": "Surabaya",
        "rating": 4.6
    },
    {
        "id": "f8kdk3j82kf8w1w817",
        "name": "Rawon Setan",
        "description": "Rawon dengan daging yang empuk dan kuah yang kaya rasa.",
        "pictureId": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT-6A7xpne5gS6lbZICHnLfynNY-_58xh_qrw&s",
        "city": "Surabaya",
        "rating": 4.7
    },
    {
        "id": "f8kdk3j81gf8w1e867",
        "name": "Sate Babi Bawah Pohon",
        "description": "Sate babi dengan bumbu khas Bali yang meresap.",
        "pictureId": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSXTjws2h3qCla54BOsgJqrwB5OzORRpSQGuA&s",
        "city": "Bali",
        "rating": 4.8
    },
    {
        "id": "f2ilk3j82kf8w1e867",
        "name": "Nasi Padang Sederhana",
        "description": "Nasi padang dengan beragam lauk yang lezat dan bumbu yang kaya.",
        "pictureId": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTYN7dCyoGgoaJkTQuFG8DyDxLuZYnylxm6Rg&s",
        "city": "Padang",
        "rating": 4.5
    },
    {
        "id": "7fkdk3j82kf8w1e867",
        "name": "Bale Udang Mang Engking",
        "description": "Restoran dengan suasana pedesaan yang menyajikan hidangan udang segar.",
        "pictureId": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ6aEAPIqhT3znY6ClBgKLh-AOdYRA2SQR0QQ&s",
        "city": "Bandung",
        "rating": 4.6
    },
    {
        "id": "f8alc3j82kf8w1e867",
        "name": "Tahu Gejrot Pak John",
        "description": "Tahu gejrot dengan kuah pedas manis yang nikmat.",
        "pictureId": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQDqCT1PZaCRRsUCswV4pbhsFsxW782LkkDCDwgbR_TXRZkEYceIHugWdj-IBf8ufCgAJ8&usqp=CAU",
        "city": "Cirebon",
        "rating": 4.4
    },
    {
        "id": "f8kdk3j82kf8w1q777",
        "name": "Mie Kocok Mang Dadeng",
        "description": "Mie kocok dengan kuah kaldu yang gurih dan kikil yang empuk.",
        "pictureId": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRY4Y4kBqSqoBVcnPflwLTEQK3byi0HifhA5A&s",
        "city": "Bandung",
        "rating": 4.5
    },
    {
        "id":"f8alc3j14sf8w1e867",
        "name": "Nasi Liwet Wongso Lemu",
        "description": "Nasi liwet khas Solo dengan cita rasa yang autentik.",
        "pictureId": "https://awsimages.detik.net.id/community/media/visual/2021/12/05/nasi-liwet-bu-wongso-lemu-2.jpeg?w=3264",
        "city": "Solo",
        "rating": 4.7
    },
    {
        "id": "f2xlc3j82kf8w1e867",
        "name": "Tahu Sumedang Renyah",
        "description": "Tahu Sumedang yang gurih dan renyah di luar, lembut di dalam.",
        "pictureId": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR-XbeaECSJxGfsMUTS-jfY3rM4ri9wDj4H7A&s",
        "city": "Sumedang",
        "rating": 4.4
    },
    {
        "id": "f8alc3l90kf8w1e867",
        "name": "Es Campur Pak Oyen",
        "description": "Es campur dengan beragam isian yang menyegarkan dan manis.",
        "pictureId": "https://assets.promediateknologi.id/crop/0x0:0x0/750x500/webp/photo/2022/04/25/1103737014.jpg",
        "city": "Bandung",
        "rating": 4.6
    },
    {
        "id": "m1alc3j82kf8w1e867",
        "name": "Kerak Telor Bang Ino",
        "description": "Kerak telor khas Betawi dengan rasa yang autentik.",
        "pictureId": "https://i.gojekapi.com/darkroom/gofood-indonesia/v2/images/uploads/081df485-ed86-43a7-a5ce-98d6d4587576.jpg",
        "city": "Jakarta",
        "rating": 4.5
    },
    {
        "id": "b4alc3j82kf8w1e867",
        "name": "Soto Lamongan Cak Har",
        "description": "Soto Lamongan dengan kuah yang kaya rempah dan daging ayam yang empuk.",
        "pictureId": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQbVzQZC4pF5K5e8-0vTFQRk3g80RZoCjw-7w&s",
        "city": "Surabaya",
        "rating": 4.7
    },
    {
        "id": "l9alc3j82kf8w1e867",
        "name": "Bakso President",
        "description": "Bakso dengan kuah kaldu yang gurih dan bakso yang kenyal.",
        "pictureId": "hhttps://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS7nlkx9sXesFmDWE-DmyoMVuMCrfMefQBmpg&s",
        "city": "Malang",
        "rating": 4.6
    },
    {
        "id": "o7alc3j82kf8w1e867",
        "name": "Nasi Krawu Mbuk Su",
        "description": "Nasi krawu dengan beragam lauk yang lezat dan bumbu yang kaya.",
        "pictureId": "https://static.promediateknologi.id/crop/0x0:0x0/750x500/webp/photo/p1/1053/2024/03/14/krawu-legen-1697157603.jpg",
        "city": "Gresik",
        "rating": 4.7
    },
    {
        "id": "k3alc3j82kf8w1e867",
        "name": "Nasi Goreng Kambing Kebon Sirih",
        "description": "Nasi goreng kambing dengan bumbu rempah yang khas dan daging kambing yang empuk.",
        "pictureId": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTNygkQFPvr_VE6Q60fMpwMJHsnsn39KXOnqw&s",
        "city": "Jakarta",
        "rating": 4.5
    },
    {
        "id": "f2zlc3j82kf8w1e867",
        "name": "Es Teler 77",
        "description": "Es teler dengan campuran buah dan susu yang segar dan nikmat.",
        "pictureId": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQZbhRpSKFF3yB-24vHLwnatlbbzxwuA48SLw&s",
        "city": "Jakarta",
        "rating": 4.4
    }
]


details = {
    "rqdv5juczeskfw1e867": {
        "id": "rqdv5juczeskfw1e867",
        "name": "Sate Khas Senayan",
        "description": "Restoran yang menyajikan berbagai macam sate khas Indonesia dengan cita rasa autentik.",
        "city": "Jakarta",
        "address": "Jl. Iskandarsyah II No.7, Kebayoran Baru, Jakarta Selatan",
        "pictureId": "https://www.centralparkjakarta.com/wp-content/uploads/2017/11/sate-khas-senayan-photo.jpg",
        "categories": [
            {"name": "Indonesian"},
            {"name": "Satay"}
        ],
        "menus": {
            "foods": [
                {"name": "Sate Ayam"},
                {"name": "Sate Kambing"}
            ],
            "drinks": [
                {"name": "Es Teh Manis"},
                {"name": "Jus Jeruk"}
            ]
        },
        "rating": 4.5,
        "customerReviews": [
            {
                "review_id": str(uuid.uuid4()),
                "name": "Budi",
                "review": "Sate yang sangat lezat, bumbu kacangnya mantap!",
                "date": "20 Maret 2022"
            }
        ]
    },
    "s1knt6za9kkfw1e867": {
        "id": "s1knt6za9kkfw1e867",
        "name": "Bebek Tepi Sawah",
        "description": "Restoran yang terkenal dengan hidangan bebek goreng dan suasana khas pedesaan Bali.",
        "city": "Bali",
        "address": "Jl. Raya Goa Gajah, Ubud, Bali",
        "pictureId": "https://tse4.mm.bing.net/th?id=OIP.we148eEHaNmEnPLLc1W7PgHaE6&pid=Api&P=0&h=180",
        "categories": [
            {"name": "Indonesian"},
            {"name": "Bebek"}
        ],
        "menus": {
            "foods": [
                {"name": "Bebek Goreng"},
                {"name": "Bebek Bakar"}
            ],
            "drinks": [
                {"name": "Es Kelapa Muda"},
                {"name": "Jus Alpukat"}
            ]
        },
        "rating": 4.7,
        "customerReviews": [
            {
                "review_id": str(uuid.uuid4()),
                "name": "Sari",
                "review": "Bebek gorengnya sangat renyah dan bumbunya meresap!",
                "date": "15 Februari 2022"
            }
        ]
    },
    "w9pga3s2tubfw1e867": {
        "id": "w9pga3s2tubfw1e867",
        "name": "Bakmi GM",
        "description": "Restoran terkenal dengan berbagai macam bakmi yang lezat dan harga terjangkau.",
        "city": "Jakarta",
        "address": "Jl. Gajah Mada No.92, Jakarta Barat",
        "pictureId": "https://tse1.mm.bing.net/th?id=OIP.YmRPnM95xRYjkP5_yIEuyAHaFj&pid=Api&P=0&h=180",
        "categories": [
            {"name": "Chinese"},
            {"name": "Bakmi"}
        ],
        "menus": {
            "foods": [
                {"name": "Bakmi Ayam"},
                {"name": "Pangsit Goreng"}
            ],
            "drinks": [
                {"name": "Es Teh Manis"},
                {"name": "Jus Melon"}
            ]
        },
        "rating": 4.3,
        "customerReviews": [
            {
                "review_id": str(uuid.uuid4()),
                "name": "Andi",
                "review": "Bakmi yang sangat enak, pangsit gorengnya wajib dicoba!",
                "date": "10 Januari 2022"
            }
        ]
    },
    "udwgdjse2wpfw1e867": {
        "id": "udwgdjse2wpfw1e867",
        "name": "Nasi Uduk Ibu Sum",
        "description": "Nasi uduk legendaris dengan sambal yang pedas dan lezat.",
        "city": "Jakarta",
        "address": "Jl. Kebon Kacang No. 15, Tanah Abang, Jakarta Pusat",
        "pictureId": "https://tse1.mm.bing.net/th?id=OIP.RaA56Xl2m5xhbptaDqm0ewHaFi&pid=Api&P=0&h=180",
        "categories": [
            {"name": "Indonesian"},
            {"name": "Nasi Uduk"}
        ],
        "menus": {
            "foods": [
                {"name": "Nasi Uduk"},
                {"name": "Ayam Goreng"}
            ],
            "drinks": [
                {"name": "Es Teh Manis"},
                {"name": "Es Jeruk"}
            ]
        },
        "rating": 4.6,
        "customerReviews": [
            {
                "review_id": str(uuid.uuid4()),
                "name": "Dewi",
                "review": "Nasi uduknya enak, sambalnya pedasnya pas!",
                "date": "5 April 2022"
            }
        ]
    },
    "uewifjw6w0jfw1e867": {
        "id": "uewifjw6w0jfw1e867",
        "name": "Warung Lela",
        "description": "Warung makan yang terkenal dengan mie ayamnya yang nikmat.",
        "city": "Bandung",
        "address": "Jl. Kopo Bihbul No.45, Bandung",
        "pictureId": "https://tse2.mm.bing.net/th?id=OIP.6pOzk7fS9zEWLh-JNn1GCAHaEK&pid=Api&P=0&h=180",
        "categories": [
            {"name": "Indonesian"},
            {"name": "Mie Ayam"}
        ],
        "menus": {
            "foods": [
                {"name": "Mie Ayam"},
                {"name": "Mie Yamin"}
            ],
            "drinks": [
                {"name": "Es Teh Manis"},
                {"name": "Es Jeruk"}
            ]
        },
        "rating": 4.4,
        "customerReviews": [
            {
                "review_id": str(uuid.uuid4()),
                "name": "Rian",
                "review": "Mie ayamnya enak banget, porsinya juga banyak!",
                "date": "12 Maret 2022"
            }
        ]
    },
    "un76djsir7rfw1e867": {
        "id": "un76djsir7rfw1e867",
        "name": "Mie Ayam Tumini",
        "description": "Mie ayam dengan porsi besar dan cita rasa yang khas.",
        "city": "Yogyakarta",
        "address": "Jl. Imogiri Timur No.187, Umbulharjo, Yogyakarta",
        "pictureId": "https://tse2.mm.bing.net/th?id=OIP.-ZfRS8VsFfJQ1gXsgDB6MAHaE7&pid=Api&P=0&h=180",
        "categories": [
            {"name": "Indonesian"},
            {"name": "Mie Ayam"}
        ],
        "menus": {
            "foods": [
                {"name": "Mie Ayam"},
                {"name": "Mie Ayam Bakso"}
            ],
            "drinks": [
                {"name": "Es Teh Manis"},
                {"name": "Es Jeruk"}
            ]
        },
        "rating": 4.8,
        "customerReviews": [
            {
                "review_id": str(uuid.uuid4()),
                "name": "Joko",
                "review": "Mie ayamnya mantap, porsinya besar banget!",
                "date": "25 Februari 2022"
            }
        ]
    },
    "s2jz3kdj92kfw1e867": {
        "id": "s2jz3kdj92kfw1e867",
        "name": "Soto Betawi Haji Husein",
        "description": "Soto Betawi dengan kuah santan yang gurih dan daging yang empuk.",
        "city": "Jakarta",
        "address": "Jl. Padang Panjang No.6, Manggarai, Jakarta Selatan",
        "pictureId": "https://tse1.mm.bing.net/th?id=OIP.Sp6MxWz4QBf6Yg8uNANCjwHaEZ&pid=Api&P=0&h=180",
        "categories": [
            {"name": "Indonesian"},
            {"name": "Soto"}
        ],
        "menus": {
            "foods": [
                {"name": "Soto Betawi"},
                {"name": "Soto Ayam"}
            ],
            "drinks": [
                {"name": "Es Teh Manis"},
                {"name": "Jus Alpukat"}
            ]
        },
        "rating": 4.5,
        "customerReviews": [
            {
                "review_id": str(uuid.uuid4()),
                "name": "Lina",
                "review": "Soto Betawinya enak, kuahnya gurih dan dagingnya empuk!",
                "date": "10 Januari 2022"
            }
        ]
    },
    "9jdm2kd92j2fw1e867": {
        "id": "9jdm2kd92j2fw1e867",
        "name": "Ayam Bakar Wong Solo",
        "description": "Ayam bakar dengan bumbu khas Solo yang meresap hingga ke tulang.",
        "city": "Solo",
        "address": "Jl. Slamet Riyadi No.300, Solo",
        "pictureId": "https://tse1.mm.bing.net/th?id=OIP.GxyrdpkWO2NnGD8sRDkZrAHaFj&pid=Api&P=0&h=180",
        "categories": [
            {"name": "Indonesian"},
            {"name": "Ayam Bakar"}
        ],
        "menus": {
            "foods": [
                {"name": "Ayam Bakar"},
                {"name": "Ayam Goreng"}
            ],
            "drinks": [
                {"name": "Es Teh Manis"},
                {"name": "Es Jeruk"}
            ]
        },
        "rating": 4.6,
        "customerReviews": [
            {
                "review_id": str(uuid.uuid4()),
                "name": "Wahyu",
                "review": "Ayam bakarnya mantap, bumbunya meresap banget!",
                "date": "18 Februari 2022"
            }
        ]
    },
    "f3jd8kdj83kf3w1e867": {
        "id": "f3jd8kdj83kf3w1e867",
        "name": "Pempek Pak Raden",
        "description": "Pempek Palembang asli dengan kuah cuko yang kental dan pedas.",
        "city": "Palembang",
        "address": "Jl. Merdeka No.45, Palembang",
        "pictureId": "https://tse1.mm.bing.net/th?id=OIP.BIDbT7vfmlfiAVLg57ejIgHaFb&pid=Api&P=0&h=180",
        "categories": [
            {"name": "Indonesian"},
            {"name": "Pempek"}
        ],
        "menus": {
            "foods": [
                {"name": "Pempek Kapal Selam"},
                {"name": "Pempek Lenjer"}
            ],
            "drinks": [
                {"name": "Es Teh Manis"},
                {"name": "Es Kacang Merah"}
            ]
        },
        "rating": 4.7,
        "customerReviews": [
            {
                "review_id": str(uuid.uuid4()),
                "name": "Rina",
                "review": "Pempeknya enak banget, cuko-nya pedas dan mantap!",
                "date": "5 Maret 2022"
            }
        ]
    },
    "f8kdk3j82kf8w1e867": {
        "id": "f8kdk3j82kf8w1e867",
        "name": "Gudeg Yu Djum",
        "description": "Gudeg asli Yogyakarta dengan cita rasa manis dan gurih yang khas.",
        "city": "Yogyakarta",
        "address": "Jl. Wijilan No.167, Yogyakarta",
        "pictureId": "https://tse3.mm.bing.net/th?id=OIP.SimA76WBMTCvbJzUPhMb7AHaE8&pid=Api&P=0&h=180",
        "categories": [
            {"name": "Indonesian"},
            {"name": "Gudeg"}
        ],
        "menus": {
            "foods": [
                {"name": "Gudeg"},
                {"name": "Krecek"}
            ],
            "drinks": [
                {"name": "Es Teh Manis"},
                {"name": "Jus Jeruk"}
            ]
        },
        "rating": 4.9,
        "customerReviews": [
            {
                "review_id": str(uuid.uuid4()),
                "name": "Ayu",
                "review": "Gudegnya enak banget, rasa manis dan gurihnya pas!",
                "date": "12 Januari 2022"
            }
        ]
    },
    
    "f4kdk3j82kf8w1e821": {
        "id": "f4kdk3j82kf8w1e821",
        "name": "Ayam Goreng Suharti",
        "description": "Ayam goreng dengan bumbu kremes yang renyah dan lezat.",
        "city": "Yogyakarta",
        "pictureId": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS54iDgi9s9EpMRpb5Y8Ofrd2JR9qfi7bZ7VA&s",
        "rating": 4.5,
        "categories": [
            {"name": "Indonesian"},
            {"name": "Ayam Goreng"}
        ],
        "menus": {
            "foods": [
                {"name": "Ayam Goreng"},
                {"name": "Nasi Putih"}
            ],
            "drinks": [
                {"name": "Es Teh Manis"},
                {"name": "Es Jeruk"}
            ]
        },
        "customerReviews": [
            {
                "review_id": "rwf4kdk3j82kf8w1e821",
                "name": "Siti",
                "review": "Ayam gorengnya sangat enak, bumbunya meresap sampai ke tulang!",
                "date": "15 Februari 2023"
            },
            {
                "review_id": "rwf4kdk3j82kf8w1e822",
                "name": "Budi",
                "review": "Portion is great and the taste is fantastic!",
                "date": "10 January 2023"
            }
        ]
    },
    "f2bdk3j82kf8w1e867": {
        "id": "f2bdk3j82kf8w1e867",
        "name": "Bubur Ayam Barito",
        "description": "Bubur ayam dengan topping melimpah dan cita rasa gurih.",
        "city": "Jakarta",
        "pictureId": "https://manual.co.id/wp-content/uploads/2014/06/Bubur-Ayam-Barito-Street-Food_Barito-1.jpg",
        "rating": 4.4,
        "categories": [
            {"name": "Indonesian"},
            {"name": "Bubur Ayam"}
        ],
        "menus": {
            "foods": [
                {"name": "Bubur Ayam"},
                {"name": "Kerupuk"}
            ],
            "drinks": [
                {"name": "Es Teh Manis"},
                {"name": "Es Campur"}
            ]
        },
        "customerReviews": [
            {
                "review_id": "rwf2bdk3j82kf8w1e867",
                "name": "Ani",
                "review": "Bubur ayamnya enak, toppingnya melimpah!",
                "date": "20 Maret 2023"
            },
            {
                "review_id": "rwf2bdk3j82kf8w1e868",
                "name": "Rudi",
                "review": "Saya suka bubur ayamnya, rasanya gurih!",
                "date": "25 Februari 2023"
            }
        ]
    },
    "f8kdk4h82kf8w1e867": {
        "id": "f8kdk4h82kf8w1e867",
        "name": "Sop Buntut Cut Meutia",
        "description": "Sop buntut dengan kuah yang kaya rasa dan daging yang empuk.",
        "city": "Jakarta",
        "pictureId": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTY9F8fxZ0sAGrlzgNMvBFEOP7LuUNa2u9JVQ&s",
        "rating": 4.6,
        "categories": [
            {"name": "Indonesian"},
            {"name": "Sop Buntut"}
        ],
        "menus": {
            "foods": [
                {"name": "Sop Buntut"},
                {"name": "Nasi Putih"}
            ],
            "drinks": [
                {"name": "Es Teh Manis"},
                {"name": "Es Campur"}
            ]
        },
        "customerReviews": [
            {
                "review_id": "rwf8kdk4h82kf8w1e867",
                "name": "Dewi",
                "review": "Sop buntutnya lezat, kuahnya kaya rasa!",
                "date": "18 Februari 2023"
            }
        ]
    },
    "a2kdk3j82kf8w1e867": {
        "id": "a2kdk3j82kf8w1e867",
        "name": "Nasi Campur Bali Men Weti",
        "description": "Nasi campur Bali dengan beragam lauk yang nikmat.",
        "city": "Bali",
        "pictureId": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSLNBQQUc8aMgcyBnIUpYer_WjJHWG_o0Kaug&s",
        "rating": 4.7,
        "categories": [
            {"name": "Indonesian"},
            {"name": "Nasi Campur"}
        ],
        "menus": {
            "foods": [
                {"name": "Nasi Campur"},
                {"name": "Ayam Betutu"}
            ],
            "drinks": [
                {"name": "Es Teh Manis"},
                {"name": "Es Jeruk"}
            ]
        },
        "customerReviews": [
            {
                "review_id": "rwa2kdk3j82kf8w1e867",
                "name": "Putu",
                "review": "Nasi campurnya enak, lauknya beragam!",
                "date": "22 Januari 2023"
            }
        ]
    },
    "o9kdk3j82kf8w1e867": {
        "id": "o9kdk3j82kf8w1e867",
        "name": "Gado-Gado Boplo",
        "description": "Gado-gado dengan bumbu kacang yang kental dan lezat.",
        "city": "Jakarta",
        "pictureId": "https://d2dzi65yjecjnt.cloudfront.net/357959.jpg",
        "rating": 4.5,
        "categories": [
            {"name": "Indonesian"},
            {"name": "Gado-Gado"}
        ],
        "menus": {
            "foods": [
                {"name": "Gado-Gado"},
                {"name": "Kerupuk"}
            ],
            "drinks": [
                {"name": "Es Teh Manis"},
                {"name": "Es Campur"}
            ]
        },
        "customerReviews": [
            {
                "review_id": "rwo9kdk3j82kf8w1e867",
                "name": "Siska",
                "review": "Gado-gadonya enak, bumbunya pas!",
                "date": "5 Maret 2023"
            }
        ]
    },
    "f8kdk3j82kf8w1c917": {
        "id": "f8kdk3j82kf8w1c917",
        "name": "Lontong Balap Garuda Pak Gendut",
        "description": "Lontong balap dengan kuah yang gurih dan tahu yang lembut.",
        "city": "Surabaya",
        "pictureId": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRYVcGVwbY6h1LCScIzk7MXBpAg95J6ADWA3Q&s",
        "rating": 4.6,
        "categories": [
            {"name": "Indonesian"},
            {"name": "Lontong Balap"}
        ],
        "menus": {
            "foods": [
                {"name": "Lontong Balap"},
                {"name": "Tahu Goreng"}
            ],
            "drinks": [
                {"name": "Es Teh Manis"},
                {"name": "Es Campur"}
            ]
        },
        "customerReviews": [
            {
                "review_id": "rwf8kdk3j82kf8w1c917",
                "name": "Rita",
                "review": "Lontong balapnya enak, kuahnya gurih!",
                "date": "10 Februari 2023"
            }
        ]
    },
    "f8kdk3j82kf8w1w817": {
        "id": "f8kdk3j82kf8w1w817",
        "name": "Rawon Setan",
        "description": "Rawon dengan daging yang empuk dan kuah yang kaya rasa.",
        "city": "Surabaya",
        "pictureId": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT-6A7xpne5gS6lbZICHnLfynNY-_58xh_qrw&s",
        "rating": 4.7,
        "categories": [
            {"name": "Indonesian"},
            {"name": "Rawon"}
        ],
        "menus": {
            "foods": [
                {"name": "Rawon"},
                {"name": "Telur Asin"}
            ],
            "drinks": [
                {"name": "Es Teh Manis"},
                {"name": "Es Campur"}
            ]
        },
        "customerReviews": [
            {
                "review_id": "rwf8kdk3j82kf8w1w817",
                "name": "Dian",
                "review": "Rawonnya enak, dagingnya empuk!",
                "date": "28 Januari 2023"
            }
        ]
    },
    "f8kdk3j81gf8w1e867": {
        "id": "f8kdk3j81gf8w1e867",
        "name": "Sate Babi Bawah Pohon",
        "description": "Sate babi dengan bumbu khas Bali yang meresap.",
        "city": "Bali",
        "address": "Jl. Gajah Mada No. 45, Denpasar, Bali",
        "pictureId": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSXTjws2h3qCla54BOsgJqrwB5OzORRpSQGuA&s",
        "categories": [
            {"name": "Indonesian"},
            {"name": "Satay"}
        ],
        "menus": {
            "foods": [
                {"name": "Sate Babi"},
                {"name": "Sate Lilit"}
            ],
            "drinks": [{"name": "Es Teh Manis"},
                {"name": "Es Cincau"}]
        },
        "rating": 4.8,
        "customerReviews": [{
                "review_id": str(uuid.uuid4()),
                "name": "Sri",
                "review": "Satenya enak banget, dagingnya empuk!",
                "date": "25 Maret 2023"
            }]
    },
    "f2ilk3j82kf8w1e867": {
        "id": "f2ilk3j82kf8w1e867",
        "name": "Nasi Padang Sederhana",
        "description": "Nasi padang dengan beragam lauk yang lezat dan bumbu yang kaya.",
        "city": "Padang",
        "address": "Jl. Padang Baru No. 12, Padang",
        "pictureId": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTYN7dCyoGgoaJkTQuFG8DyDxLuZYnylxm6Rg&s",
        "categories": [
            {"name": "Indonesian"},
            {"name": "Padang"}
        ],
        "menus": {
            "foods": [
                {"name": "Nasi Padang"},
                {"name": "Rendang"}
            ],
            "drinks": [{"name": "Es Teh Manis"},
                {"name": "Es Cincau"}]
        },
        "rating": 4.5,
        "customerReviews": [{
                "review_id": str(uuid.uuid4()),
                "name": "Sri",
                "review": "Rendangnya enak banget, dagingnya empuk!",
                "date": "25 Maret 2023"
            }]
    },
    "7fkdk3j82kf8w1e867": {
        "id": "7fkdk3j82kf8w1e867",
        "name": "Bale Udang Mang Engking",
        "description": "Restoran dengan suasana pedesaan yang menyajikan hidangan udang segar.",
        "city": "Bandung",
        "address": "Jl. Cihampelas No. 14, Bandung",
        "pictureId": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ6aEAPIqhT3znY6ClBgKLh-AOdYRA2SQR0QQ&s",
        "categories": [
            {"name": "Indonesian"},
            {"name": "Seafood"}
        ],
        "menus": {
            "foods": [
                {"name": "Udang Bakar"},
                {"name": "Udang Goreng Tepung"}
            ],
            "drinks": [{"name": "Es Teh Manis"},
                {"name": "Es Cincau"}]
        },
        "rating": 4.6,
        "customerReviews": [{
                "review_id": str(uuid.uuid4()),
                "name": "Sri",
                "review": "Udangnya enak banget, dagingnya empuk!",
                "date": "25 Maret 2023"
            }]
    },
    "f8alc3j82kf8w1e867": {
        "id": "f8alc3j82kf8w1e867",
        "name": "Tahu Gejrot Pak John",
        "description": "Tahu gejrot dengan kuah pedas manis yang nikmat.",
        "city": "Cirebon",
        "address": "Jl. Cirebon Utara No. 5, Cirebon",
        "pictureId": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQDqCT1PZaCRRsUCswV4pbhsFsxW782LkkDCDwgbR_TXRZkEYceIHugWdj-IBf8ufCgAJ8&usqp=CAU",
        "categories": [
            {"name": "Indonesian"},
            {"name": "Tahu Gejrot"}
        ],
        "menus": {
            "foods": [
                {"name": "Tahu Gejrot"},
                {"name": "Tahu Sumedang"}
            ],
            "drinks": [{"name": "Es Teh Manis"},
                {"name": "Es Cincau"}]
        },
        "rating": 4.4,
        "customerReviews": [{
                "review_id": str(uuid.uuid4()),
                "name": "Sri",
                "review": "Tahunya enak banget, dagingnya empuk!",
                "date": "25 Maret 2023"
            }]
    },
    "f8kdk3j82kf8w1q777": {
        "id": "f8kdk3j82kf8w1q777",
        "name": "Mie Kocok Mang Dadeng",
        "description": "Mie kocok dengan kuah kaldu yang gurih dan kikil yang empuk.",
        "city": "Bandung",
        "address": "Jl. Kebon Sirih No. 23, Bandung",
        "pictureId": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRY4Y4kBqSqoBVcnPflwLTEQK3byi0HifhA5A&s",
        "categories": [
            {"name": "Indonesian"},
            {"name": "Noodle"}
        ],
        "menus": {
            "foods": [
                {"name": "Mie Kocok"},
                {"name": "Mie Ayam"}
            ],
            "drinks": [{"name": "Es Teh Manis"},
                {"name": "Es Cincau"}]
        },
        "rating": 4.5,
         "customerReviews": [{
                "review_id": str(uuid.uuid4()),
                "name": "Sri",
                "review": "Mienya enak banget, dagingnya empuk!",
                "date": "25 Maret 2023"
            }]
    },
    "f8alc3j14sf8w1e867": {
        "id": "f8alc3j14sf8w1e867",
        "name": "Nasi Liwet Wongso Lemu",
        "description": "Nasi liwet khas Solo dengan cita rasa yang autentik.",
        "city": "Solo",
        "address": "Jl. Slamet Riyadi No. 123, Solo",
        "pictureId": "https://awsimages.detik.net.id/community/media/visual/2021/12/05/nasi-liwet-bu-wongso-lemu-2.jpeg?w=3264",
        "categories": [
            {"name": "Indonesian"},
            {"name": "Nasi Liwet"}
        ],
        "menus": {
            "foods": [
                {"name": "Nasi Liwet"},
                {"name": "Ayam Goreng"}
            ],
            "drinks": [{"name": "Es Teh Manis"},
                {"name": "Es Cincau"}]
        },
        "rating": 4.7,
        "customerReviews": [{
                "review_id": str(uuid.uuid4()),
                "name": "Sri",
                "review": "Dagingya enak banget, dagingnya empuk!",
                "date": "25 Maret 2023"
            }]
    },
    "f2xlc3j82kf8w1e867": {
        "id": "f2xlc3j82kf8w1e867",
        "name": "Tahu Sumedang Renyah",
        "description": "Tahu Sumedang yang gurih dan renyah di luar, lembut di dalam.",
        "city": "Sumedang",
        "address": "Jl. Raya Sumedang No. 78, Sumedang",
        "pictureId": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR-XbeaECSJxGfsMUTS-jfY3rM4ri9wDj4H7A&s",
        "categories": [
            {"name": "Indonesian"},
            {"name": "Tahu Sumedang"}
        ],
        "menus": {
            "foods": [
                {"name": "Tahu Sumedang"},
                {"name": "Tahu Goreng"}
            ],
            "drinks": [{"name": "Es Teh Manis"},
                {"name": "Es Cincau"}]
        },
        "rating": 4.4,
        "customerReviews": [{
                "review_id": str(uuid.uuid4()),
                "name": "Sri",
                "review": "Tahunya enak banget, dagingnya empuk!",
                "date": "25 Maret 2023"
            }]
    },
    "f8alc3l90kf8w1e867": {
        "id": "f8alc3l90kf8w1e867",
        "name": "Es Campur Pak Oyen",
        "description": "Es campur dengan beragam isian yang menyegarkan dan manis.",
        "city": "Bandung",
        "address": "Jl. Cibaduyut No. 15, Bandung",
        "pictureId": "https://assets.promediateknologi.id/crop/0x0:0x0/750x500/webp/photo/2022/04/25/1103737014.jpg",
        "categories": [
            {"name": "Indonesian"},
            {"name": "Dessert"}
        ],
        "menus": {
            "foods": [],
            "drinks": [
                {"name": "Es Campur"},
                {"name": "Es Teler"}
            ]
        },
        "rating": 4.6,
         "customerReviews": [{
                "review_id": str(uuid.uuid4()),
                "name": "Sri",
                "review": "Esnya enak banget, nanasnya empuk!",
                "date": "25 Maret 2023"
            }]
    },
    "m1alc3j82kf8w1e867": {
        "id": "m1alc3j82kf8w1e867",
        "name": "Kerak Telor Bang Ino",
        "description": "Kerak telor khas Betawi dengan rasa yang autentik.",
        "city": "Jakarta",
        "address": "Jl. Setiabudi No. 10, Jakarta",
        "pictureId": "https://i.gojekapi.com/darkroom/gofood-indonesia/v2/images/uploads/081df485-ed86-43a7-a5ce-98d6d4587576.jpg",
        "categories": [
            {"name": "Indonesian"},
            {"name": "Betawi"}
        ],
        "menus": {
            "foods": [
                {"name": "Kerak Telor"},
                {"name": "Ketoprak"}
            ],
            "drinks": [
                {"name": "Es Campur"},
                {"name": "Es Teler"}
            ]
        },
        "rating": 4.7,
        "customerReviews": [{
                "review_id": str(uuid.uuid4()),
                "name": "Sri",
                "review": "Telornya enak banget, nasinya empuk!",
                "date": "25 Maret 2023"
            }]
    },
    "b4alc3j82kf8w1e867": {
        "id": "b4alc3j82kf8w1e867",
        "name": "Soto Lamongan Cak Har",
        "description": "Soto Lamongan dengan kuah yang kaya rempah dan daging ayam yang empuk.",
        "city": "Surabaya",
        "address": "Jl. Setiabudi No. 10, Surabaya",
        "pictureId": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQbVzQZC4pF5K5e8-0vTFQRk3g80RZoCjw-7w&s",
        "categories": [
            {"name": "Indonesian"},
            {"name": "Soto"}
        ],
        "menus": {
            "foods": [
                {"name": "Soto Betawi"},
                {"name": "Soto Ayam"}
            ],
            "drinks": [
                {"name": "Es Campur"},
                {"name": "Es Teler"}
            ]
        },
        "rating": 4.7,
         "customerReviews": [{
                "review_id": str(uuid.uuid4()),
                "name": "Sri",
                "review": "Sotonya enak banget, nasinya empuk!",
                "date": "25 Maret 2023"
            }]
    },
    "l9alc3j82kf8w1e867": {
        "id": "l9alc3j82kf8w1e867",
        "name": "Bakso President",
        "description": "Bakso dengan kuah kaldu yang gurih dan bakso yang kenyal.",
        "city": "Malang",
        "address": "Jl. Setiabudi No. 10, Malang",
        "pictureId": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS7nlkx9sXesFmDWE-DmyoMVuMCrfMefQBmpg&s",
        "categories": [
            {"name": "Indonesian"},
            {"name": "Bakso"}
        ],
        "menus": {
            "foods": [
                {"name": "Bakso Urat"},
                {"name": "Bakso Ayam"}
            ],
            "drinks": [
                {"name": "Es Campur"},
                {"name": "Es Teler"}
            ]
        },
        "rating": 4.6,
         "customerReviews": [{
                "review_id": str(uuid.uuid4()),
                "name": "Sri",
                "review": "Baksonya enak banget, daginnya empuk!",
                "date": "25 Maret 2023"
            }]
    },
    "o7alc3j82kf8w1e867": {
        "id": "o7alc3j82kf8w1e867",
        "name": "Nasi Krawu Mbuk Su",
        "description": "Nasi krawu dengan beragam lauk yang lezat dan bumbu yang kaya.",
        "city": "Gresik",
        "address": "Jl. Slamet Riyadi No. 123, Gresik",
        "pictureId": "https://static.promediateknologi.id/crop/0x0:0x0/750x500/webp/photo/p1/1053/2024/03/14/krawu-legen-1697157603.jpg",
        "categories": [
            {"name": "Indonesian"},
            {"name": "Nasi Krawu"}
        ],
        "menus": {
            "foods": [
                {"name": "Nasi Krawu"},
                {"name": "Ayam Goreng"}
            ],
            "drinks": [{"name": "Es Teh Manis"},
                {"name": "Es Cincau"}]
        },
        "rating": 4.7,
        "customerReviews": [{
                "review_id": str(uuid.uuid4()),
                "name": "Sri",
                "review": "Dagingya enak banget, dagingnya empuk!",
                "date": "25 Maret 2023"
            }]
    },
    "k3alc3j82kf8w1e867": {
        "id": "k3alc3j82kf8w1e867",
        "name": "Nasi Goreng Kambing Kebon Sirih",
        "description": "Nasi goreng kambing dengan bumbu rempah yang khas dan daging kambing yang empuk.",
        "city": "Jakarta",
        "address": "Jl. Slamet Riyadi No. 123, Jakarta",
        "pictureId": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTNygkQFPvr_VE6Q60fMpwMJHsnsn39KXOnqw&s",
        "categories": [
            {"name": "Indonesian"},
            {"name": "Nasi Goreng"}
        ],
        "menus": {
            "foods": [
                {"name": "Nasi goreng Kambing"},
                {"name": "Ayam Goreng"}
            ],
            "drinks": [{"name": "Es Teh Manis"},
                {"name": "Es Cincau"}]
        },
        "rating": 4.5,
        "customerReviews": [{
                "review_id": str(uuid.uuid4()),
                "name": "Sri",
                "review": "Nasinya enak banget, dagingnya empuk!",
                "date": "25 Maret 2023"
            }]
    },
    "f2zlc3j82kf8w1e867": {
        "id": "f2zlc3j82kf8w1e867",
        "name": "Es Teler 77",
        "description": "Es teler dengan campuran buah dan susu yang segar dan nikmat.",
        "city": "Jakarta",
        "address": "Jl. Slamet Riyadi No. 123, Jakarta",
        "pictureId": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQZbhRpSKFF3yB-24vHLwnatlbbzxwuA48SLw&s",
        "categories": [
            {"name": "Indonesian"},
            {"name": "Es Teler"}
        ],
        "menus": {
            "foods": [
                {"name": "Nasi goreng Kambing"},
                {"name": "Ayam Goreng"}
            ],
            "drinks": [{"name": "Es Teh Manis"},
                {"name": "Es Cincau"}]
        },
        "rating": 4.4,
        "customerReviews": [{
                "review_id": str(uuid.uuid4()),
                "name": "Sri",
                "review": "Esnya enak banget, nanasnya empuk!",
                "date": "25 Maret 2023"
            }]
    }
}




