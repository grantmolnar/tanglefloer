from Modules.CTMinus import d_plus, m2, delta_ell, type_da, delta_ell_case_1, delta_ell_case_2, delta_ell_case_3, \
    delta_ell_case_4, d_mixed, d_minus
from Modules.ETangleStrands import ETangleStrands
from Modules.TypeDA import TypeDA
from SignAlgebra.AMinus import AMinus
from SignAlgebra.Z2PolynomialRing import Z2PolynomialRing, Z2Monomial
from Tangles.Tangle import ETangle


def test_apply():
    r = Z2PolynomialRing(['a', 'b'])
    f = Z2PolynomialRing.Map(r, r, {'a': 'a', 'b': 'a'})
    x = Z2Monomial(r, {'a': 1, 'b': 1}).to_polynomial()
    y = Z2Monomial(r, {'a': 2}).to_polynomial()
    assert f.apply(x) == y


def empty_da_module(etangle: ETangle):
    return TypeDA(etangle.ring, etangle.left_algebra, etangle.right_algebra,
                  etangle.left_scalar_action, etangle.right_scalar_action)


def test_d_plus():
    under1 = ETangle(ETangle.Type.UNDER, (1, 1, 1, 1), 2)
    under1_module = empty_da_module(under1)
    sd_under1_1 = ETangleStrands(under1, {0: 0, 3: 3, 4: 4}, {1: 4, 2: 3})
    sd_under1_1_out = ETangleStrands(under1, {0: 0, 3: 3, 4: 4}, {1: 3, 2: 4}).to_generator(under1_module)
    sd_under1_2 = ETangleStrands(under1, {0: 0, 2: 2, 3: 3}, {1: 3, 4: 0})
    sd_under1_2_out = under1.ring['U2'] * under1.ring['U3'] * \
                      ETangleStrands(under1, {0: 0, 2: 2, 3: 3}, {1: 0, 4: 3}).to_generator(under1_module)
    under2 = ETangle(ETangle.Type.UNDER, (1, -1, 1, 1), 2)
    under2_module = empty_da_module(under2)
    sd_under2_1 = ETangleStrands(under2, {0: 0, 3: 3, 4: 4}, {1: 4, 2: 3})
    sd_under2_1_out = ETangleStrands(under2, {0: 0, 3: 3, 4: 4}, {1: 3, 2: 4}).to_generator(under2_module)
    sd_under2_2 = ETangleStrands(under2, {0: 0, 2: 2, 3: 3}, {1: 3, 4: 0})
    sd_under2_2_out = under2_module.zero()

    over1 = ETangle(ETangle.Type.OVER, (1, 1, 1, 1), 2)
    over1_module = empty_da_module(over1)
    sd_over1_1 = ETangleStrands(over1, {4: 4, 1: 1, 3: 3}, {2: 2, 0: 4})
    sd_over1_1_out = over1.ring['U2'] * \
                     ETangleStrands(over1, {4: 4, 1: 1, 3: 3}, {0: 2, 2: 4}).to_generator(over1_module)
    sd_over1_2 = ETangleStrands(over1, {1: 1, 4: 4, 3: 3}, {2: 1, 0: 4})
    sd_over1_2_out = over1.ring['U2'] * \
                     ETangleStrands(over1, {1: 1, 4: 4, 3: 3}, {0: 1, 2: 4}).to_generator(over1_module)
    over2 = ETangle(ETangle.Type.OVER, (1, 1, -1, 1), 2)
    over2_module = empty_da_module(over2)
    sd_over2_1 = ETangleStrands(over2, {1: 1, 0: 0, 4: 4}, {3: 1, 2: 4})
    sd_over2_1_out = over2_module.zero()
    # Figure 9 from "An introduction..."
    over3 = ETangle(ETangle.Type.OVER, (1, 1, -1, -1), 2)
    over3_module = empty_da_module(over3)
    sd_over3_1 = ETangleStrands(over3, {1: 2, 2: 1, 3: 4}, {0: 1, 3: 2})
    sd_over3_1_out = over3_module.zero()

    cap1 = ETangle(ETangle.Type.CAP, (1, 1, -1, 1), 2)
    cap1_module = empty_da_module(cap1)
    sd_cap1_1 = ETangleStrands(cap1, {0: 0, 1: 1}, {4: 1, 3: 2})
    sd_cap1_1_out = cap1.ring['U3'] * ETangleStrands(cap1, {0: 0, 1: 1}, {4: 2, 3: 1}).to_generator(cap1_module)
    sd_cap1_2 = ETangleStrands(cap1, {3: 3, 1: 1}, {4: 0, 0: 2})
    sd_cap1_2_out = cap1.ring['U1'] * cap1.ring['U3'] * \
                    ETangleStrands(cap1, {3: 3, 1: 1}, {4: 2, 0: 0}).to_generator(cap1_module)

    assert d_plus(under1_module, sd_under1_1) == sd_under1_1_out
    assert d_plus(under1_module, sd_under1_2) == sd_under1_2_out
    assert d_plus(under2_module, sd_under2_1) == sd_under2_1_out
    assert d_plus(under2_module, sd_under2_2) == sd_under2_2_out

    assert d_plus(over1_module, sd_over1_1) == sd_over1_1_out
    assert d_plus(over1_module, sd_over1_2) == sd_over1_2_out
    assert d_plus(over2_module, sd_over2_1) == sd_over2_1_out
    assert d_plus(over3_module, sd_over3_1) == sd_over3_1_out

    assert d_plus(cap1_module, sd_cap1_1) == sd_cap1_1_out
    assert d_plus(cap1_module, sd_cap1_2) == sd_cap1_2_out


def test_d_minus():
    under1 = ETangle(ETangle.Type.OVER, (-1, -1, -1, -1), 2)
    under1_module = empty_da_module(under1)
    sd_under1_1 = ETangleStrands(under1, {2: 2, 4: 4}, {0: 0, 1: 1, 3: 3})
    sd_under1_1_out = under1.ring['U3'] * under1.ring['U4'] * \
                      ETangleStrands(under1, {2: 4, 4: 2}, {0: 0, 1: 1, 3: 3}).to_generator(under1_module)

    # Figure 9 from "An introduction..."
    over3 = ETangle(ETangle.Type.OVER, (1, 1, -1, -1), 2)
    over3_module = empty_da_module(over3)
    sd_over3_1 = ETangleStrands(over3, {1: 2, 2: 1, 3: 4}, {0: 1, 3: 2})
    sd_over3_1_out = over3.ring['U3'] * \
                     ETangleStrands(over3, {1: 2, 2: 4, 3: 1}, {0: 1, 3: 2}).to_generator(over3_module) + \
                     over3.ring['U3'] * \
                     ETangleStrands(over3, {1: 4, 2: 1, 3: 2}, {0: 1, 3: 2}).to_generator(over3_module)

    assert d_minus(under1_module, sd_under1_1) == sd_under1_1_out
    assert d_minus(over3_module, sd_over3_1) == sd_over3_1_out


def test_d_mixed():
    # Figure 9 from "An introduction..."
    over3 = ETangle(ETangle.Type.OVER, (1, 1, -1, -1), 2)
    over3_module = empty_da_module(over3)
    sd_over3_1 = ETangleStrands(over3, {1: 2, 2: 1, 3: 4}, {0: 1, 3: 2})

    sd_over3_1_out = over3.ring['U2'] * \
                     ETangleStrands(over3, {1: 1, 2: 2, 3: 4}, {0: 1, 3: 2}).to_generator(over3_module) + \
                     over3.ring['U2'] * over3.ring['U3'] * \
                     ETangleStrands(over3, {1: 2, 2: 3, 3: 4}, {0: 1, 1: 2}).to_generator(over3_module) + \
                     over3.ring['U3'] * \
                     ETangleStrands(over3, {1: 3, 2: 1, 3: 4}, {0: 1, 2: 2}).to_generator(over3_module) + \
                     over3.ring.one() * \
                     ETangleStrands(over3, {1: 2, 2: 1, 3: 3}, {0: 1, 4: 2}).to_generator(over3_module)

    assert d_mixed(over3_module, sd_over3_1) == sd_over3_1_out


def test_m2():
    # Figure 10 from "An introduction..."
    cap2 = ETangle(ETangle.Type.CAP, (1, -1, -1), 1)
    cap2_module = empty_da_module(cap2)
    sd_cap2_1 = ETangleStrands(cap2, {0: 0, 1: 3}, {2: 0})
    sd_cap2_1_out = ETangleStrands(cap2, {0: 0, 1: 3}, {2: 1}).to_generator(cap2_module)
    algebra1 = AMinus((-1,))
    elt1 = algebra1.generator({0: 1})
    idem = algebra1.generator({0: 0})

    assert m2(cap2_module, sd_cap2_1, elt1) == sd_cap2_1_out
    assert m2(cap2_module, sd_cap2_1, idem) == sd_cap2_1.to_generator(cap2_module)

    cup1 = ETangle(ETangle.Type.CUP, (1, -1), 1)
    cup1_module = empty_da_module(cup1)
    sd_cup1_1 = ETangleStrands(cup1, {}, {2: 1, 0: 0})
    algebra2 = AMinus((1, -1))
    idem2 = algebra2.generator({0: 0, 1: 1})
    elt = algebra2.generator({1: 0, 2: 2})
    sd_cup1_2 = ETangleStrands(cup1, {}, {2: 2, 0: 1})
    sd_cup1_2_out = cup1_module.ring['U1'] * ETangleStrands(cup1, {}, {2: 2, 0: 0}).to_generator(cup1_module)

    assert m2(cup1_module, sd_cup1_1, idem2) == sd_cup1_1.to_generator(cup1_module)
    assert m2(cup1_module, sd_cup1_2, elt) == sd_cup1_2_out

    cup2 = ETangle(ETangle.Type.CUP, (-1, 1), 1)
    cup2_module = empty_da_module(cup2)
    sd_cup2_1 = ETangleStrands(cup2, {}, {0: 0, 2: 1})
    elt2 = cup2.right_algebra.generator({0: 0, 1: 2})
    sd_cup2_1_out = cup2_module.ring['U1'] * ETangleStrands(cup2, {}, {0: 0, 2: 2}).to_generator(cup2_module)

    assert m2(cup2_module, sd_cup2_1, elt2) == sd_cup2_1_out


def test_delta_ell_case_1():
    over1 = ETangle(ETangle.Type.OVER, (-1, -1), 1)
    over1_module = empty_da_module(over1)
    x = ETangleStrands(over1, {0: 2}, {0: 0, 1: 1})
    a1 = 1
    a2 = 2
    y = x
    out = over1.left_algebra.generator({1: 2, 2: 1}).to_element() ** \
          (over1.ring['U2'] * y.to_generator(over1_module))
    assert delta_ell_case_1(over1_module, x, a1, a2) == out


def test_delta_ell_case_2():
    over1 = ETangle(ETangle.Type.OVER, (1, 1), 1)
    over1_module = empty_da_module(over1)
    x = ETangleStrands(over1, {0: 1, 1: 0}, {2: 2})
    a1 = 0
    a2 = 1
    y = ETangleStrands(over1, {0: 0, 1: 1}, {2: 2})
    out = (over1.left_algebra.ring['U1'] * over1.left_algebra.generator({2: 2}).to_element()) ** \
          y.to_generator(over1_module)
    assert delta_ell_case_2(over1_module, x, a1, a2) == out


def test_delta_ell_case_3():
    over1 = ETangle(ETangle.Type.OVER, (-1, 1), 1)
    over1_module = empty_da_module(over1)
    x = ETangleStrands(over1, {1: 1, 2: 2}, {0: 0})
    a1 = 0
    a2 = 1
    y = ETangleStrands(over1, {0: 1, 2: 2}, {0: 0})
    out = over1.left_algebra.generator({0: 1}).to_element() ** (over1.ring['U1'] * y.to_generator(over1_module))
    assert delta_ell_case_3(over1_module, x, a1, a2) == out


def test_delta_ell_case_4():
    over1 = ETangle(ETangle.Type.OVER, (-1, -1), 1)
    over1_module = empty_da_module(over1)
    x = ETangleStrands(over1, {0: 1, 1: 0}, {2: 2})
    a1 = 0
    a2 = 2
    y = ETangleStrands(over1, {2: 1, 1: 0}, {2: 2})
    out = over1.left_algebra.generator({2: 0}).to_element() ** (over1.ring['U2'] * y.to_generator(over1_module))
    assert delta_ell_case_4(over1_module, x, a1, a2) == out


def test_delta_ell():
    over1 = ETangle(ETangle.Type.OVER, (-1, -1, 1), 2)
    over1_module = empty_da_module(over1)
    x = ETangleStrands(over1, {1: 0, 2: 1}, {3: 0, 2: 2})
    y = ETangleStrands(over1, {0: 0, 2: 1}, {3: 0, 2: 2})
    c = over1.ring.one()
    elt = over1.left_algebra.generator({0: 1, 3: 3}).to_element()
    out = elt ** (c * y.to_generator(over1_module))
    assert delta_ell(over1_module, x) == out


def test_type_da():
    cup = ETangle(ETangle.Type.CUP, (-1, 1), 1)
    cup_da = type_da(cup)
    da_list = [cup_da]
    for da in da_list:
        assert len(da.graph.nodes) == 12
        assert len(da.decomposed()) == 2


def test_isomorphism():
    cup = ETangle(ETangle.Type.CUP, (1, -1), 1)
    cup_da = type_da(cup)
    cap = ETangle(ETangle.Type.CAP, (1, -1), 1)
    cap_da = type_da(cap)
    assert cup_da.is_isomorphic_to(cup_da)
    assert not cup_da.is_isomorphic_to(cup_da[1, 0])
    assert not cup_da.is_isomorphic_to(cap_da)


def test_halve():
    cup = ETangle(ETangle.Type.CUP, (1, -1), 1)
    cup_da = type_da(cup).reduce()
    cap = ETangle(ETangle.Type.CAP, (1, -1), 1)
    cap_da = type_da(cap).reduce()
    unknot_da = (cup_da ** cap_da).reduce()
    unknot_da = unknot_da.identify_variables('U1b', 'U1c')
    unknot_da = unknot_da.halve()
    assert len(unknot_da.graph.nodes()) == 4

# def test_cap():
#     cap_da = type_da(ETangle(ETangle.Type.CAP, (-1, 1), 1))
#     cap_da.to_agraph(idempotents=False).draw('output/test_cap.svg')

# def test_identity_bimodule():
#     idempotents = False
#
#     r = ETangle(ETangle.Type.STRAIGHT, (1,))
#     r_da = type_da(r)
#     r_da.to_agraph(idempotents=idempotents).draw('output/identity_bimodules/r.svg')
#     r_da.reduce().to_agraph(idempotents=idempotents).draw('output/identity_bimodules/r_reduced.svg')
#
#     for l in sublists(list(range(len(r.left_algebra.ss)))):
#         for g in r.left_algebra.left_gens(l):
#             print(f"{g}: {g.to_element().maslov()}, {g.to_element().two_alexander()}")

# l = ETangle(ETangle.Type.STRAIGHT, (-1,))
# l_da = type_da(l)
# l_da.to_agraph(idempotents=idempotents).draw('output/identity_bimodules/l.svg')
# l_da.reduce().to_agraph(idempotents=idempotents).draw('output/identity_bimodules/l_reduced.svg')
#
# rr = ETangle(ETangle.Type.STRAIGHT, (1, 1))
# rr_da = type_da(rr)
# rr_da.to_agraph(idempotents=idempotents).draw('output/identity_bimodules/rr.svg')
# rr_da.reduce().to_agraph(idempotents=idempotents).draw('output/identity_bimodules/rr_reduced.svg')
#
# rl = ETangle(ETangle.Type.STRAIGHT, (1, -1))
# rl_da = type_da(rl)
# rl_da.to_agraph(idempotents=idempotents).draw('output/identity_bimodules/rl.svg')
# rl_da.reduce().to_agraph(idempotents=idempotents).draw('output/identity_bimodules/rl_reduced.svg')
#
# lr = ETangle(ETangle.Type.STRAIGHT, (-1, 1))
# lr_da = type_da(lr)
# lr_da.to_agraph(idempotents=idempotents).draw('output/identity_bimodules/lr.svg')
# lr_da.reduce().to_agraph(idempotents=idempotents).draw('output/identity_bimodules/lr_reduced.svg')
#
# ll = ETangle(ETangle.Type.STRAIGHT, (-1, -1))
# ll_da = type_da(ll)
# ll_da.to_agraph(idempotents=idempotents).draw('output/identity_bimodules/ll.svg')
# ll_da.reduce().to_agraph(idempotents=idempotents).draw('output/identity_bimodules/ll_reduced.svg')

# def test_tensor():
#         idempotents = False
#         cup = ETangle(ETangle.Type.CAP, (-1, 1), 1)
#         cup_da = type_da(cup)
#         straight_da = type_da(ETangle(ETangle.Type.STRAIGHT, (-1, 1)))
#         unknot_long_da = (straight_da ** cup_da).reduce()
#         unknot_long_da.to_agraph(idempotents=idempotents).draw('output/test_cup.svg')
#         unknot_long_da = unknot_long_da.simplify_homotopic_variables('U1a', 'U1b')
#         unknot_long_da = unknot_long_da.reduce()
#         unknot_long_da.to_agraph(idempotents=idempotents).draw('output/test_cup1.svg')
#         unknot_long_da = unknot_long_da.simplify_homotopic_variables('U1a', 'U1c')
#         unknot_long_da = unknot_long_da.reduce()
#         unknot_long_da.to_agraph(idempotents=idempotents).draw('output/test_cup2.svg')
#         unknot_long_da = unknot_long_da.simplify_homotopic_variables('U1a', 'U3a')
#         unknot_long_da = unknot_long_da.reduce()
#         unknot_long_da.to_agraph(idempotents=idempotents).draw('output/test_cup_s.svg')

# def test_tensor():
#         idempotents = False
#         cup = ETangle(ETangle.Type.CUP, (-1, 1), 1)
#         cap = ETangle(ETangle.Type.CAP, (-1, 1), 1)
#         cup_da = type_da(cup)
#         cup_da.to_agraph(idempotents=idempotents).draw('output/cup.svg')
#         cap_da = type_da(cap)
#         cup_da.to_agraph(idempotents=idempotents).draw('output/cap.svg')
#         unknot_long_da = (cup_da ** cap_da).reduce()
#         unknot_long_da.to_agraph(idempotents=idempotents).draw('output/unknot_simplified.svg')

# def test_tensor():
#     idempotents = False
#     cap = ETangle(ETangle.Type.CAP, (-1, 1), 1)
#     cap_da = type_da(cap).reduce()
#     cap_da.to_agraph(idempotents=idempotents).draw('output/test1.svg')
#     straight = ETangle(ETangle.Type.STRAIGHT, (-1, 1))
#     straight_da = type_da(straight).reduce()
#     unknot_da = (straight_da ** cap_da).reduce()
#     unknot_da.to_agraph(idempotents=idempotents).draw('output/test2.svg')
#     unknot_da = unknot_da.identify_variables('U1a', 'U1b')
#     unknot_da.to_agraph(idempotents=idempotents).draw('output/test3.svg')
#     unknot_da = unknot_da.identify_variables('U1a', 'U1c')
#     unknot_da.to_agraph(idempotents=idempotents).draw('output/test4.svg')
#     unknot_da = unknot_da.identify_variables('U1a', 'U3a')
#     unknot_da.to_agraph(idempotents=idempotents).draw('output/test5.svg')

# def test_simplify():
#     idempotents = False
#     cup = ETangle(ETangle.Type.CUP, (-1, 1), 1)
#     cup_da = type_da(cup)
#     cup_da.to_agraph(idempotents=idempotents).draw('output/cup.svg')
#     cup_da[2, -2].to_agraph(idempotents=idempotents).draw('output/cup_shift.svg')
#     cup_da = cup_da.reduce()
#     cup_da.to_agraph(idempotents=idempotents).draw('output/cup_r.svg')
#
#     cap = ETangle(ETangle.Type.CAP, (-1, 1), 1)
#     cap_da = type_da(cap)
#     cap_da.to_agraph(idempotents=idempotents).draw('output/cap.svg')
#     cap_da = cap_da.reduce()
#     cap_da.to_agraph(idempotents=idempotents).draw('output/cap_r.svg')
#     cap_da = cap_da.identify_variables('U1', 'U2')
#     cap_da.to_agraph(idempotents=idempotents).draw('output/cap_rs.svg')
#
#     unknot_da = cup_da ** cap_da
#     unknot_da.to_agraph(idempotents=idempotents).draw('output/unknot.svg')

# def test_tensor2():
#     idempotents = False
#     straight = ETangle(ETangle.Type.STRAIGHT, (1,))
#     straight_da = type_da(straight).reduce()
#     da = (straight_da ** straight_da).reduce()
#     da.to_agraph(idempotents=idempotents).draw('output/test_straight_da.svg')

# def test_type_da_reduced():
# idempotents = False
#
# # some simple examples
# cup = ETangle(ETangle.Type.CUP, (1, -1), 1)
# over = ETangle(ETangle.Type.OVER, (1, -1), 1)
# cap = ETangle(ETangle.Type.CAP, (-1, 1), 1)
#
# cup_da = type_da(cup)
# cup_da_reduced = cup_da.reduce()
# over_da = type_da(over)
# over_da_reduced = over_da.reduce()
# cap_da = type_da(cap)
# cap_da_reduced = cap_da.reduce()
# cap_da.to_agraph(idempotents=False).draw('output/cap_da.svg')
# cap_da_reduced.to_agraph(idempotents=True).draw('output/cap_da_reduced.svg')
#
# (cup_da_reduced ** (over_da_reduced ** cap_da_reduced)) \
#     .to_agraph(idempotents=idempotents).draw('output/test0.svg')
# (cup_da_reduced ** (over_da_reduced ** cap_da_reduced)).to_chain_complex().write_m2_def('output/test0.m2')
# ((cup_da_reduced ** over_da_reduced) ** cap_da_reduced) \
#     .to_agraph(idempotents=idempotents).draw('output/test1.svg')
# ((cup_da_reduced ** over_da_reduced) ** cap_da_reduced).to_chain_complex().write_m2_def('output/test1.m2')

# def test_trefoil():
#     t1 = ETangle(ETangle.Type.CUP, (-1, 1), 1)
#     t2 = ETangle(ETangle.Type.CUP, (-1, 1, -1, 1), 3)
#     t3 = ETangle(ETangle.Type.OVER, (-1, 1, -1, 1), 2)
#     t4 = ETangle(ETangle.Type.UNDER, (-1, -1, 1, 1), 1)
#     t5 = ETangle(ETangle.Type.OVER, (-1, -1, 1, 1), 2)
#     t6 = ETangle(ETangle.Type.CAP, (-1, 1, -1, 1), 1)
#     t7 = ETangle(ETangle.Type.CAP, (-1, 1), 1)
#
#     idempotents = False
#     t1_da = type_da(t1).reduce()
#     print(len(t1_da.graph.nodes()))
#     t2_da = type_da(t2).reduce()
#     print(len(t2_da.graph.nodes()))
#     t12_da = (t1_da ** t2_da)
#     print(len(t12_da.graph.nodes()))
#     t12_da = t12_da.reduce()
#     print(len(t12_da.graph.nodes()))
#     print(t12_da.ring.variables)
# t12_da.to_agraph(idempotents=idempotents).draw('output/test_trefoil.svg')

# def test_priority():
#     t = ETangle(ETangle.Type.CAP, (1, -1), 1)
#     da = type_da(t)
#     da_reduced = da.priority_reduced()
#     da_reduced.to_agraph(idempotents=False).draw('output/test_pool.svg')

# def test_timer():
#     print(timeit.timeit('trial1()', setup='from Test.ModulesTests import TestCTMinus', number=1))
#     print(timeit.timeit('trial2()', setup='from Test.ModulesTests import TestCTMinus', number=1))
#
# @staticmethod
# def trial1():
#     cup = ETangle(ETangle.Type.CUP, (1, -1), 1)
#     over = ETangle(ETangle.Type.OVER, (1, -1), 1)
#     cap = ETangle(ETangle.Type.CAP, (-1, 1), 1)
#     t = cup + over + cap
#     da = reduced_type_da(t)
#
# @staticmethod
# def trial2():
#     cup = ETangle(ETangle.Type.CUP, (1, -1), 1)
#     over = ETangle(ETangle.Type.OVER, (1, -1), 1)
#     cap = ETangle(ETangle.Type.CAP, (-1, 1), 1)
#     t = cup + over + cap
#     da = reduced_type_da2(t)

# def test_test():
#     t1 = ETangle(ETangle.Type.CUP, (1, -1), 1)
#     t2 = ETangle(ETangle.Type.OVER, (1, -1), 1)
#     t3 = ETangle(ETangle.Type.UNDER, (1, -1), 1)
#     t4 = ETangle(ETangle.Type.CAP, (1, -1), 1)
#     t = t1 + t2 + t3 + t4
#     da = reduced_type_da(t)
#     da.to_agraph().draw('output/test.svg')

# def test_macaulay2():
#     cup = ETangle(ETangle.Type.CUP, (1, -1), 1)
#     cup_da = type_da(cup)
#     over = ETangle(ETangle.Type.OVER, (1, -1), 1)
#     over_da = type_da(over)
#     cap = ETangle(ETangle.Type.CAP, (-1, 1), 1)
#     cap_da = type_da(cap)
#     unknot_da_tt = cup_da ** over_da ** cap_da
#     unknot_da_tt.to_agraph(idempotents=False).draw('output/test_unknot_tt.svg')
#     unknot_da_ttr = unknot_da_tt.reduce()
#     unknot_da_ttr.to_agraph(idempotents=False).draw('output/test_unknot_ttr.svg')
#     unknot_da_ttr.write_m2_def('output/unknot_da_ttr.m2')
