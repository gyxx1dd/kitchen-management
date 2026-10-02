from django.contrib.auth.mixins import UserPassesTestMixin


class StaffRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        if self.request.user.is_staff:
            return True
        return False
