import logging
import stripe
from subscriptions.models import StripeCustomer

from django.conf import settings

MONTH = 'm'
ANNUAL = 'a'

API_KEY = settings.STRIPE_SECRET_KEY
logger = logging.getLogger(__name__)


class SubMonthPlan:
    def __init__(self):
        self.stripe_plan_id = settings.STRIPE_PLAN_MONTHLY_ID
        self.amount = 699


class SubAnnualPlan:
    def __init__(self):
        self.stripe_plan_id = settings.STRIPE_PLAN_ANNUAL_ID
        self.amount = 6990


class SubPlan:
    def __init__(self, plan_id):
        """
        plan_id is either string 'm' (stands for monthly)
        or a string letter 'a' (which stands for annual)
        """
        if plan_id == MONTH:
            self.plan = SubMonthPlan()
            self.id = MONTH
        elif plan_id == ANNUAL:
            self.plan = SubAnnualPlan()
            self.id = ANNUAL
        else:
            raise ValueError('Invalid plan_id value')

        self.currency = 'gbp'

    @property
    def stripe_plan_id(self):
        return self.plan.stripe_plan_id

    @property
    def amount(self):
        return self.plan.amount
