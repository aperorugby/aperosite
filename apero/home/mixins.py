
class ActiveTabMixin(object):

    active_tab = None
    
    def get_context_data(self, **kwargs):
        ctx = super(ActiveTabMixin, self).get_context_data(**kwargs)
        ctx.setdefault("active_tab", self.active_tab)
        return ctx
