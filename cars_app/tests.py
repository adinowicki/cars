import random
from unittest import mock

import faker
import faker_vehicle
from django import test

from . import models

fake = faker.Faker()
fake.add_provider(faker_vehicle.VehicleProvider)


class TestCarsViewSet(test.TestCase):
    valid_nhtsa_return = {
        "Count": 47,
        "Message": "Response returned successfully",
        "SearchCriteria": "Make:volkswagen",
        "Results": [
            {
                "Make_ID": 482,
                "Make_Name": "VOLKSWAGEN",
                "Model_ID": 1951,
                "Model_Name": "Routan",
            },
            {
                "Make_ID": 482,
                "Make_Name": "VOLKSWAGEN",
                "Model_ID": 3133,
                "Model_Name": "Golf",
            },
            {
                "Make_ID": 482,
                "Make_Name": "VOLKSWAGEN",
                "Model_ID": 3134,
                "Model_Name": "Passat",
            },
            {
                "Make_ID": 482,
                "Make_Name": "VOLKSWAGEN",
                "Model_ID": 3135,
                "Model_Name": "Phaeton",
            },
            {
                "Make_ID": 482,
                "Make_Name": "VOLKSWAGEN",
                "Model_ID": 3136,
                "Model_Name": "Touareg",
            },
            {
                "Make_ID": 482,
                "Make_Name": "VOLKSWAGEN",
                "Model_ID": 3137,
                "Model_Name": "Jetta",
            },
            {
                "Make_ID": 482,
                "Make_Name": "VOLKSWAGEN",
                "Model_ID": 3140,
                "Model_Name": "GTI",
            },
            {
                "Make_ID": 482,
                "Make_Name": "VOLKSWAGEN",
                "Model_ID": 3141,
                "Model_Name": "R32",
            },
            {
                "Make_ID": 482,
                "Make_Name": "VOLKSWAGEN",
                "Model_ID": 3142,
                "Model_Name": "Jetta Wagon",
            },
            {
                "Make_ID": 482,
                "Make_Name": "VOLKSWAGEN",
                "Model_ID": 4084,
                "Model_Name": "Rabbit",
            },
            {
                "Make_ID": 482,
                "Make_Name": "VOLKSWAGEN",
                "Model_ID": 4085,
                "Model_Name": "New GTI",
            },
            {
                "Make_ID": 482,
                "Make_Name": "VOLKSWAGEN",
                "Model_ID": 4167,
                "Model_Name": "Eos",
            },
            {
                "Make_ID": 482,
                "Make_Name": "VOLKSWAGEN",
                "Model_ID": 5059,
                "Model_Name": "Golf SportWagen",
            },
            {
                "Make_ID": 482,
                "Make_Name": "VOLKSWAGEN",
                "Model_ID": 8051,
                "Model_Name": "Golf III",
            },
            {
                "Make_ID": 482,
                "Make_Name": "VOLKSWAGEN",
                "Model_ID": 8052,
                "Model_Name": "Jetta III",
            },
            {
                "Make_ID": 482,
                "Make_Name": "VOLKSWAGEN",
                "Model_ID": 8053,
                "Model_Name": "Corrado",
            },
            {
                "Make_ID": 482,
                "Make_Name": "VOLKSWAGEN",
                "Model_ID": 8055,
                "Model_Name": "EuroVan",
            },
            {
                "Make_ID": 482,
                "Make_Name": "VOLKSWAGEN",
                "Model_ID": 8118,
                "Model_Name": "e-Golf",
            },
            {
                "Make_ID": 482,
                "Make_Name": "VOLKSWAGEN",
                "Model_ID": 8119,
                "Model_Name": "Beetle",
            },
            {
                "Make_ID": 482,
                "Make_Name": "VOLKSWAGEN",
                "Model_ID": 8121,
                "Model_Name": "CC",
            },
            {
                "Make_ID": 482,
                "Make_Name": "VOLKSWAGEN",
                "Model_ID": 8151,
                "Model_Name": "Tiguan",
            },
            {
                "Make_ID": 482,
                "Make_Name": "VOLKSWAGEN",
                "Model_ID": 8364,
                "Model_Name": "Jetta SportWagen",
            },
            {
                "Make_ID": 482,
                "Make_Name": "VOLKSWAGEN",
                "Model_ID": 8460,
                "Model_Name": "Cabrio",
            },
            {
                "Make_ID": 482,
                "Make_Name": "VOLKSWAGEN",
                "Model_ID": 8486,
                "Model_Name": "New Cabrio",
            },
            {
                "Make_ID": 482,
                "Make_Name": "VOLKSWAGEN",
                "Model_ID": 8487,
                "Model_Name": "New Golf",
            },
            {
                "Make_ID": 482,
                "Make_Name": "VOLKSWAGEN",
                "Model_ID": 8488,
                "Model_Name": "New Jetta",
            },
            {
                "Make_ID": 482,
                "Make_Name": "VOLKSWAGEN",
                "Model_ID": 13670,
                "Model_Name": "Golf GTI",
            },
            {
                "Make_ID": 482,
                "Make_Name": "VOLKSWAGEN",
                "Model_ID": 13844,
                "Model_Name": "Golf R",
            },
            {
                "Make_ID": 482,
                "Make_Name": "VOLKSWAGEN",
                "Model_ID": 14216,
                "Model_Name": "CABRIOLET",
            },
            {
                "Make_ID": 482,
                "Make_Name": "VOLKSWAGEN",
                "Model_ID": 14217,
                "Model_Name": "FOX",
            },
            {
                "Make_ID": 482,
                "Make_Name": "VOLKSWAGEN",
                "Model_ID": 14261,
                "Model_Name": "Quantum",
            },
            {
                "Make_ID": 482,
                "Make_Name": "VOLKSWAGEN",
                "Model_ID": 14262,
                "Model_Name": "Scirocco",
            },
            {
                "Make_ID": 482,
                "Make_Name": "VOLKSWAGEN",
                "Model_ID": 14266,
                "Model_Name": "Vanagon",
            },
            {
                "Make_ID": 482,
                "Make_Name": "VOLKSWAGEN",
                "Model_ID": 14568,
                "Model_Name": "Dasher",
            },
            {
                "Make_ID": 482,
                "Make_Name": "VOLKSWAGEN",
                "Model_ID": 14569,
                "Model_Name": "KOMBI",
            },
            {
                "Make_ID": 482,
                "Make_Name": "VOLKSWAGEN",
                "Model_ID": 17618,
                "Model_Name": "Atlas",
            },
            {
                "Make_ID": 482,
                "Make_Name": "VOLKSWAGEN",
                "Model_ID": 24230,
                "Model_Name": "Golf Alltrack",
            },
            {
                "Make_ID": 482,
                "Make_Name": "VOLKSWAGEN",
                "Model_ID": 24247,
                "Model_Name": "Tiguan Limited",
            },
            {
                "Make_ID": 482,
                "Make_Name": "VOLKSWAGEN",
                "Model_ID": 25871,
                "Model_Name": "Arteon",
            },
            {
                "Make_ID": 482,
                "Make_Name": "VOLKSWAGEN",
                "Model_ID": 26088,
                "Model_Name": "GLI",
            },
            {
                "Make_ID": 482,
                "Make_Name": "VOLKSWAGEN",
                "Model_ID": 27124,
                "Model_Name": "Atlas Cross Sport",
            },
            {
                "Make_ID": 482,
                "Make_Name": "VOLKSWAGEN",
                "Model_ID": 28219,
                "Model_Name": "ID.4",
            },
            {
                "Make_ID": 482,
                "Make_Name": "VOLKSWAGEN",
                "Model_ID": 28652,
                "Model_Name": "Taos",
            },
            {
                "Make_ID": 482,
                "Make_Name": "VOLKSWAGEN",
                "Model_ID": 29590,
                "Model_Name": "Atlas Cross Sport 4Motion",
            },
            {
                "Make_ID": 482,
                "Make_Name": "VOLKSWAGEN",
                "Model_ID": 29591,
                "Model_Name": "Tiguan 4Motion",
            },
            {
                "Make_ID": 482,
                "Make_Name": "VOLKSWAGEN",
                "Model_ID": 29592,
                "Model_Name": "Atlas 4Motion",
            },
            {
                "Make_ID": 482,
                "Make_Name": "VOLKSWAGEN",
                "Model_ID": 29595,
                "Model_Name": "Taos 4Motion",
            },
        ],
    }

    def test_post_nonexistent_make(self):
        with mock.patch("requests.post") as mocked_post:
            data = mock.MagicMock()
            data.return_value = {
                "Count": 0,
                "Message": "Response returned successfully",
                "SearchCriteria": "Make:nonexistent",
                "Results": [],
            }
            post = mock.MagicMock()
            post.json = data
            post.status_code = 200
            mocked_post.return_value = post
            c = test.Client()
            make = "Nonexistent"
            model = "Golf"
            response = c.post(
                "/cars/",
                data={
                    "make": make,
                    "model": model,
                },
                content_type="application/json",
            )
            self.assertEqual(response.status_code, 400)
            self.assertIn("make", response.json())
            self.assertFalse(
                models.Car.objects.filter(
                    make=make,
                    model=model,
                ).exists()
            )

    def test_post_nonexistent_model(self):
        with mock.patch("requests.post") as mocked_post:
            data = mock.MagicMock()
            data.return_value = self.valid_nhtsa_return
            post = mock.MagicMock()
            post.json = data
            post.status_code = 200
            mocked_post.return_value = post
            c = test.Client()
            make = "Volkswagen"
            model = "Nonexistent"
            response = c.post(
                "/cars/",
                data={
                    "make": make,
                    "model": model,
                },
                content_type="application/json",
            )
            self.assertEqual(response.status_code, 400)
            self.assertIn("model", response.json())
            self.assertFalse(
                models.Car.objects.filter(
                    make=make,
                    model=model,
                ).exists()
            )

    def test_post_valid_cars(self):
        with mock.patch("requests.post") as mocked_post:
            data = mock.MagicMock()
            data.return_value = self.valid_nhtsa_return
            post = mock.MagicMock()
            post.json = data
            post.status_code = 200
            mocked_post.return_value = post
            c = test.Client()
            make = "Volkswagen"
            for model in "Golf", "Passat":
                self.assertFalse(
                    models.Car.objects.filter(
                        make=make,
                        model=model,
                    ).exists()
                )
                response = c.post(
                    "/cars/",
                    data={
                        "make": make,
                        "model": model,
                    },
                    content_type="application/json",
                )
                self.assertEqual(response.status_code, 201)
                self.assertTrue(
                    models.Car.objects.filter(
                        make=make,
                        model=model,
                    ).exists()
                )

    def test_post_double(self):
        with mock.patch("requests.post") as mocked_post:
            data = mock.MagicMock()
            data.return_value = self.valid_nhtsa_return
            post = mock.MagicMock()
            post.json = data
            post.status_code = 200
            mocked_post.return_value = post
            c = test.Client()
            make = "Volkswagen"
            model = "Golf"
            models.Car.objects.create(
                make=make,
                model=model,
            )
            response = c.post(
                "/cars/",
                data={
                    "make": make,
                    "model": model,
                },
                content_type="application/json",
            )
            self.assertEqual(response.status_code, 400)
            self.assertIn("non_field_errors", response.json())

    def test_delete_nonexistent(self):
        pk = 1
        self.assertFalse(
            models.Car.objects.filter(
                pk=pk,
            ).exists()
        )
        c = test.Client()
        response = c.delete(
            f"/cars/{pk}/",
            content_type="application/json",
            follow=True,
        )
        self.assertEqual(response.status_code, 404)

    def test_delete_existing(self):
        car = fake.vehicle_object()
        pk = models.Car.objects.create(
            make=car["Make"],
            model=car["Model"],
        ).pk
        c = test.Client()
        response = c.delete(
            f"/cars/{pk}/",
            content_type="application/json",
            follow=True,
        )
        self.assertEqual(response.status_code, 204)
        self.assertFalse(
            models.Car.objects.filter(
                pk=pk,
            ).exists()
        )

    def test_get_empty(self):
        c = test.Client()
        response = c.get("/cars/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), [])

    def test_get_list(self):
        cars = []
        for _ in range(10):
            car = fake.vehicle_object()
            obj, created = models.Car.objects.get_or_create(
                make=car["Make"],
                model=car["Model"],
            )
            if created:
                cars.append((obj.pk, car))
        models.Rate.objects.create(
            car_id=cars[-1][0],
            rating=4,
        )
        models.Rate.objects.create(
            car_id=cars[-1][0],
            rating=3,
        )
        result = [
            {
                "id": pk,
                "make": car["Make"],
                "model": car["Model"],
                "avg_rating": None,
            }
            for pk, car in cars
        ]
        result[-1]["avg_rating"] = 3.5
        c = test.Client()
        response = c.get("/cars/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), result)

    def test_get_avg(self):
        car = fake.vehicle_object()
        pk = models.Car.objects.create(
            make=car["Make"],
            model=car["Model"],
        ).pk
        s = 0
        ratings = 100
        for _ in range(ratings):
            rating = random.randint(1, 5)
            models.Rate.objects.create(
                car_id=pk,
                rating=rating,
            )
            s += rating
        c = test.Client()
        response = c.get("/cars/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 1)
        self.assertAlmostEqual(
            response.json()[0]["avg_rating"],
            s / ratings,
            places=1,
        )


class TestRateViewSet(test.TestCase):
    def test_post_non_valid(self):
        car = fake.vehicle_object()
        pk = models.Car.objects.create(
            make=car["Make"],
            model=car["Model"],
        ).pk
        c = test.Client()
        for rating in [
            "one",
            0,
            6,
            3.5,
        ]:
            response = c.post(
                "/rate/",
                data={
                    "car_id": pk,
                    "rating": rating,
                },
                content_type="application/json",
            )
            self.assertEqual(response.status_code, 400)
            self.assertIn("rating", response.json())
            try:
                self.assertFalse(
                    models.Rate.objects.filter(
                        car_id=pk,
                        rating=rating,
                    ).exists()
                )
            except ValueError:
                continue
        pk = 1
        rating = 5
        self.assertFalse(
            models.Car.objects.filter(
                pk=pk,
            ).exists()
        )
        response = c.post(
            "/rate/",
            data={
                "car_id": pk,
                "rating": rating,
            },
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 400)
        self.assertIn("car_id", response.json())
        self.assertFalse(
            models.Rate.objects.filter(
                car_id=pk,
                rating=rating,
            ).exists()
        )

    def test_post_valid(self):
        car = fake.vehicle_object()
        pk = models.Car.objects.create(
            make=car["Make"],
            model=car["Model"],
        ).pk
        c = test.Client()
        for rating in (3, 4):
            n = random.randrange(100)
            for _ in range(n):
                response = c.post(
                    "/rate/",
                    data={
                        "car_id": pk,
                        "rating": rating,
                    },
                    content_type="application/json",
                )
                self.assertEqual(response.status_code, 201)
            self.assertEqual(
                models.Rate.objects.filter(
                    car_id=pk,
                    rating=rating,
                ).count(),
                n,
            )


class TestPopularViewSet(test.TestCase):
    def test_get_empty(self):
        c = test.Client()
        response = c.get("/popular/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), [])

    def test_get_list(self):
        cars = []
        for _ in range(10):
            car = fake.vehicle_object()
            obj, created = models.Car.objects.get_or_create(
                make=car["Make"],
                model=car["Model"],
            )
            if created:
                cars.append((obj.pk, car))
        models.Rate.objects.create(
            car_id=cars[0][0],
            rating=4,
        )
        models.Rate.objects.create(
            car_id=cars[0][0],
            rating=3,
        )
        result = [
            {
                "id": pk,
                "make": car["Make"],
                "model": car["Model"],
                "rates_number": 0,
            }
            for pk, car in cars
        ]
        result[0]["rates_number"] = 2
        c = test.Client()
        response = c.get("/popular/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), result)

    def test_rates_number(self):
        result = []
        for _ in range(10):
            car = fake.vehicle_object()
            rates = random.randrange(100)
            obj, created = models.Car.objects.get_or_create(
                make=car["Make"],
                model=car["Model"],
            )
            if created:
                for _ in range(rates):
                    models.Rate.objects.create(
                        car_id=obj.pk,
                        rating=random.randint(1, 5),
                    )
                result.append((obj.pk, rates))
        result.sort(key=lambda x: (-x[1], x[0]))
        c = test.Client()
        response = c.get("/popular/")
        self.assertEqual(response.status_code, 200)
        for i, car in enumerate(response.json()):
            self.assertEqual(car["id"], result[i][0])
            self.assertEqual(car["rates_number"], result[i][1])
