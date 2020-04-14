# from django import forms
#
# # 产品数量选择
# PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]
#
#
# class CartAddProductForm(forms.Form):
#     # quantity 限制用户选择数量为20个
#     quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES, coerce=int)
#     # 指定当前数量是增加False还是替换原有数量True
#     update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)
#
