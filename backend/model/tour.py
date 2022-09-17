class Tour:


    def __init__(self, tour_id, guide_id, route_id, day_of_week, price_per_person_in_cents, tour_name, inactive):

        self.tour_id = tour_id
        self.guide_id = guide_id
        self.route_id = route_id
        self.day_of_week = day_of_week
        self.price_per_person_in_cents = price_per_person_in_cents
        self.inactive = inactive
        self.tour_name = tour_name

    def to_dict(self):
        return {
            "tour_id": self.tour_id,
            "guide_id": self.guide_id,
            "day_of_week": self.day_of_week,
            "route_id": self.route_id,
            "price_per_person_in_cents": f"${self.price_per_person_in_cents/100}",
            "tour_name":self.tour_name,
            "inactive": self.inactive,
        }
