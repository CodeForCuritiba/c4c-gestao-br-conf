from django.db.models import FloatField, IntegerField
from django.db.models.aggregates import Aggregate

__all__ = [
    'CovarPop', 'Corr', 'RegrAvgX', 'RegrAvgY', 'RegrCount', 'RegrIntercept',
    'RegrR2', 'RegrSlope', 'RegrSXX', 'RegrSXY', 'RegrSYY', 'StatAggregate',
]


class StatAggregate(Aggregate):
    def __init__(self, y, x, output_field=FloatField()):
        if not x or not y:
            raise ValueError('Both y and x must be provided.')
        super().__init__(y, x, output_field=output_field)

    def resolve_expression(self, query=None, allow_joins=True, reuse=None, summarize=False, for_save=False):
        return super().resolve_expression(query, allow_joins, reuse, summarize)


class Corr(StatAggregate):
    function = 'CORR'


class CovarPop(StatAggregate):
    def __init__(self, y, x, sample=False):
        self.function = 'COVAR_SAMP' if sample else 'COVAR_POP'
        super().__init__(y, x)


class RegrAvgX(StatAggregate):
    function = 'REGR_AVGX'


class RegrAvgY(StatAggregate):
    function = 'REGR_AVGY'


class RegrCount(StatAggregate):
    function = 'REGR_COUNT'

    def __init__(self, y, x):
        super().__init__(y=y, x=x, output_field=IntegerField())

    def convert_value(self, value, expression, connection, context):
        if value is None:
            return 0
        return int(value)


class RegrIntercept(StatAggregate):
    function = 'REGR_INTERCEPT'


class RegrR2(StatAggregate):
    function = 'REGR_R2'


class RegrSlope(StatAggregate):
    function = 'REGR_SLOPE'


class RegrSXX(StatAggregate):
    function = 'REGR_SXX'


class RegrSXY(StatAggregate):
    function = 'REGR_SXY'


class RegrSYY(StatAggregate):
    function = 'REGR_SYY'
