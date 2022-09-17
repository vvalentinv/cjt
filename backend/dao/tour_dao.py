from util.db_connection import pool
from model.tour import Tour


class TourDao:

    def add_poi(self, pois):
        with pool.connection() as conn:
            with conn.cursor() as cur:
                cur.execute("INSERT INTO tour_routes (poi_arr) VALUES (%s) RETURNING id", (pois,))
                tour_row = cur.fetchone()
            return tour_row[0]

    def add_tour(self, tour):
        with pool.connection() as conn:
            with conn.cursor() as cur:
                cur.execute("INSERT INTO tours "
                            "(route_id, guide_id, day_of_week, "
                            "price_per_person_in_cents, title, inactive) VALUES"
                            "(%s, %s, %s, %s, %s, %s) RETURNING *", (tour.route_id, tour.guide_id, tour.day_of_week,
                                                                     int(float(tour.price_per_person_in_cents) * 100), tour.tour_name,
                                                                     tour.inactive))
                tour_row = cur.fetchone()
                if tour_row:
                    id = tour_row[0]
                    route_id = tour_row[1]
                    guide_id = tour_row[2]
                    day = tour_row[3]
                    price = tour_row[4]
                    tour_name = tour_row[5]
                    inactive = tour_row[6]
                    return Tour(id, route_id, guide_id, day, price, tour_name, inactive)
                else:
                    return None

    def get_tour(self):
        tour_list = []
        with pool.connection() as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT STRING_AGG(poi_name, '--') AS route_name,  t.title, CONCAT(u.first_name, ' ',"
                            " u.last_name) AS guide_name, t.day_of_week, t.price_per_person_in_cents "
                            "FROM route_points_of_interest rpoi "
                            "JOIN tour_routes tr ON rpoi.id = ANY(tr.poi_arr) "
                            "JOIN tours t ON t.route_id = tr.id "
                            "JOIN users u ON u.id = t.guide_id "
                            "WHERE inactive IS false "
                            "GROUP BY  t.guide_id, t.day_of_week, t.price_per_person_in_cents, "
                            "u.first_name, u.last_name, t.title")
                for row in cur:
                    tour = [row[0], row[1], row[2], row[3], row[4]]
                    tour_list.append(tour)
                return tour_list

    def get_tours_by_id(self, used_id):
        tour_list = []
        with pool.connection() as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT STRING_AGG(poi_name, '--') AS route_name,  t.title, CONCAT(u.first_name, ' ',"
                            " u.last_name) AS guide_name, t.day_of_week, t.price_per_person_in_cents, t.id "
                            "FROM route_points_of_interest rpoi "
                            "JOIN tour_routes tr ON rpoi.id = ANY(tr.poi_arr) "
                            "JOIN tours t ON t.route_id = tr.id "
                            "JOIN users u ON u.id = t.guide_id "
                            "WHERE guide_id = %s"
                            "GROUP BY  t.guide_id, t.day_of_week, t.price_per_person_in_cents, "
                            "u.first_name, u.last_name, t.title, t.id", (used_id,))
                for row in cur:
                    tour = [row[0], row[1], row[2], row[3], row[4], row[5]]
                    tour_list.append(tour)
                return tour_list

    def update_tour(self, tour):
        if tour.inactive is "1":
            inactive = True
        else:
            inactive = False
        with pool.connection() as conn:
            with conn.cursor() as cur:
                cur.execute("UPDATE tours SET price_per_person_in_cents = %s, day_of_week = %s, inactive = %s "
                            "WHERE id = %s RETURNING *", (int(float(tour.price_per_person_in_cents) * 100),
                                                          tour.day_of_week, inactive, tour.tour_id))
                tour_row = cur.fetchone()
                if tour_row is None:
                    return None
                else:
                    updated_tour = Tour(tour_row[0], tour_row[1], tour_row[2], tour_row[3], tour_row[4],
                                        tour_row[5], tour_row[6])

                    return updated_tour

    def delete_tour(self, tour_id):
        with pool.connection() as conn:
            with conn.cursor() as cur:
                cur.execute("DELETE FROM tours WHERE id = %s", (tour_id,))
                row_deleted = cur.rowcount
                if row_deleted != 1:
                    return False
                else:
                    return True


