def aggregation_personalizado():
    return [
    {
        "$unwind": {
            "path": "$variations"
        }
    },
    {
        "$group": {
            "_id": "$_id",
            "code": {
                "$first": "$code"
            },
            "country": {
                "$first": "$countryCode"
            },
            "categoryCode": {
                "$first": "$product.categoryCode"
            },
            "brand": {
                "$first": "$product.brand.name"
            },
            "model": {
                "$first": "$product.model"
            },
            "year": {
                "$first": "$product.year"
            },
            "price_base": {
                "$first": "$price.base"
            },
            "price_currency": {
                "$first": "$price.currencyCode"
            },
            "price_net": {
                "$first": "$price.net"
            },
            "installment_currency": {
                "$first": "$defaultInstallmentPlan.currencyCode"
            },
            "installment_number": {
                "$first": "$defaultInstallmentPlan.installments"
            },
            "installment_amount_per_installment": {
                "$first": "$defaultInstallmentPlan.amountPerInstallment"
            },
            "installment_downpayment": {
                "$first": "$defaultInstallmentPlan.downPayment"
            },
            "installment_anual_rate": {
                "$first": "$defaultInstallmentPlan.annualRate"
            },
            "installment_variable_downpayment": {
                "$first": "$defaultInstallmentPlan.variableDownPayment"
            },
            "colors": {
                "$push": {
                    "$concat": "$variations.color"
                }
            },
            "stock": {
                "$push": {
                    "$concat": {
                        "$toString": "$variations.stock"
                    }
                }
            },
            "published": {
                "$first": "$published"
            }
        }
    }
]