##
# @brief Calculate and print year-1 revenue, cost, and profit from US and EU
#
# @param gamers Number of gamers in millions
# @param nongamers Number of non-gamers in millions
# @param gamer_conversion Fraction of gamers that converts to Stadia
# @param nongamer_conversion Fraction of non-gamers that converts to Stadia
#
# @return 
def run_year1(gamers, nongamers, gamer_conversion, nongamer_conversion):
    # Calculate total users
    users = gamers * gamer_conversion + nongamers * nongamer_conversion
    print("----------------------------------------")
    print("Num users: {}M".format(users))

    # 
    rev_youtube = 1.2 * .25 * 20 * 0.06 * 365

    # Revenue from royalties = #users * $15 per game * two games per year
    rev_royalty = users * 15 * 2

    # Revenue from subscriptions: Assume 2/3rd users pay for subscription.
    # Revenue per subscription is $10 per month * 12 months per year
    rev_subscriptions = users * (2./3) * 10 * 12

    # Total revenue in year one
    rev_total = rev_youtube + rev_royalty + rev_subscriptions

    # Cost of providing streaming = users * 8 hours per week * 52 weeks per year
    # * 3 cents per hour of streaming
    cost_streaming =  users * 8 * 52 * 0.03

    # Cost of datacenters: Assume each user plays for 8 hours per week. Each
    # server runs for 168 hours per week (24 * 7). Number of servers is
    # therefore (users * 8 / 168). Each server costs $500.
    cost_computing_fixed =  users * 8 / 168. * 500

    # Variable cost of computing: Number of servers times XXX?
    cost_computing_var = users * 8 / 168. * 168 * 2 * 0.01

    # Marketing cost
    cost_marketing = 88.34 + 1.1

    cost_total = cost_streaming + cost_computing_fixed + cost_computing_var + cost_marketing
    print("----------------------------------------")

    print("Rev YouTube: {}M".format(round(rev_youtube, 2)))
    print("Rev Royalty {}M".format(round(rev_royalty, 2)))
    print("Rev Subscriptions {}M".format(round(rev_subscriptions, 2)))
    print("Cost Streaming {}M".format(round(cost_streaming, 2)))
    print("Cost Computing fixed {}M".format(round(cost_computing_fixed, 2)))
    print("Cost Computing var {}M".format(round(cost_computing_var, 2)))
    print("Cost Marketing {}M".format(round(cost_marketing, 2)))

    print("----------------------------------------")

    print("Cost: {}M".format(round(cost_total, 2)))
    print("Revenue: {}M".format(round(rev_total, 2)))
    print("Profit: {}M".format(round(rev_total - cost_total, 2)))

##
# @brief Calculate and print cost and revenue in the APAC region
#
# @param num_asia_users: Number of users in the APAC region
def run_asia(num_asia_users):
    users = num_asia_users
    rev_youtube = 1.2 * .25 * 20 * 0.06 * 365
    rev_royalty = users * 15 * 2
    rev_subscriptions = users / 2. * 10 * 12

    rev_total = rev_youtube + rev_royalty + rev_subscriptions

    cost_streaming =  users * 8 * 52 * 0.03
    cost_computing_fixed =  users * 8 / 168. * 500
    cost_computing_var = users * 8 / 168. * 168 * 2 * 0.01
    cost_marketing = 88.34 + 1.1
    cost_marketing_asia = 110.

    cost_total = cost_streaming + cost_computing_fixed + cost_computing_var + cost_marketing + cost_marketing_asia

    print("====================================================")

    print("Asia Cost: {}M".format(round(cost_total, 2)))
    print("Asia Revenue: {}M".format(round(rev_total, 2)))
    print("Asia Profit: {}M".format(round(rev_total - cost_total, 2)))

def run_googlefi(num_googlefi):

    rev_googlefi = 4 * 52 * 0.5
    rev_total = rev_googlefi * 0.2 # 20% profit margins
    cost_total = 0

    print("-------------------------------------------------")

    print("Mobile Cost: {}M".format(round(cost_total, 2)))
    print("Mobile Revenue: {}M".format(round(rev_total, 2)))
    print("Mobile Profit: {}M".format(round(rev_total - cost_total, 2)))

def run_nextgen(gamers, nongamers, gamer_conversion, nongamer_conversion, num_asia_users):
    users = gamers * gamer_conversion + nongamers * nongamer_conversion + num_asia_users
    print("Num users: {}M".format(users))

    rev_youtube = 1.2 * .25 * 20 * 0.06 * 365
    rev_royalty = users * 15 * 2
    rev_subscriptions = users * (2./3) * 10 * 12

    rev_total = rev_youtube + rev_royalty + rev_subscriptions

    cost_streaming =  users * 8 * 52 * 0.03
    cost_computing_fixed =  users * 8 / 168. * 500
    cost_computing_var = users * 8 / 168. * 168 * 2 * 0.01
    cost_marketing = 88.34 + 1.1

    cost_total = cost_streaming + cost_computing_fixed + cost_computing_var + cost_marketing

    print("----------------------------------------")

    print("VR Cost: {}M".format(round(cost_total, 2)))
    print("VR Revenue: {}M".format(round(rev_total, 2)))
    print("VR Profit: {}M".format(round(rev_total - cost_total, 2)))

if __name__ == "__main__":

    # Assuming total population in NAC and EMEA is 700 M
    gamers = 400. * 0.3
    nongamers = 300. * 0.15
    gamer_conversion = 0.05 #2./6
    nongamer_conversion = 0.08 #2./5
    num_asia_users = 14.
    print("\n**********YEAR1**************\n")
    run_year1(gamers, nongamers, gamer_conversion, nongamer_conversion)
    print("\n**********ASIA**************\n")
    run_asia(num_asia_users)
    print("\n**********MOBILE**************\n")
    run_googlefi(4)
    print("\n**********VR**************\n")

    vr_gamer_conversion = gamer_conversion * .24
    vr_nongamer_conversion = nongamer_conversion * .24
    run_nextgen(gamers, nongamers, vr_gamer_conversion, vr_nongamer_conversion, num_asia_users * .24)

