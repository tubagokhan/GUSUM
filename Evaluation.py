# -*- coding: utf-8 -*-
"""
Created on Tue Dec 28 16:10:48 2021

@author: TUBA
"""

import rouge

def prepare_results(m, p, r, f):
    return '\t{}:\t{}: {:5.2f}\t{}: {:5.2f}\t{}: {:5.2f}'.format(m, 'P', 100.0 * p, 'R', 100.0 * r, 'F1', 100.0 * f)

def rougeEvaluation(all_hypothesis, all_references):

    for aggregator in ['Avg']:
        print('Evaluation with {}'.format(aggregator))
        apply_avg = aggregator == 'Avg'
        apply_best = aggregator == 'Best'
    
        evaluator = rouge.Rouge(metrics=['rouge-n', 'rouge-l', 'rouge-w'],
                               max_n=4,
                               limit_length=False,
                               length_limit=1000,
                               length_limit_type='words',
                               apply_avg=apply_avg,
                               apply_best=apply_best,
                               alpha=0.2, # Default F1_score
                               weight_factor=1.2,
                               stemming=True)
    
        scores = evaluator.get_scores(all_hypothesis, all_references)
    
        for metric, results in sorted(scores.items(), key=lambda x: x[0]):
            if not apply_avg and not apply_best: # value is a type of list as we evaluate each summary vs each reference
                for hypothesis_id, results_per_ref in enumerate(results):
                    nb_references = len(results_per_ref['p'])
                    for reference_id in range(nb_references):
                        print('\tHypothesis #{} & Reference #{}: '.format(hypothesis_id, reference_id))
                        print('\t' + prepare_results(metric,results_per_ref['p'][reference_id], results_per_ref['r'][reference_id], results_per_ref['f'][reference_id]))
                print()
            else:
                print(prepare_results(metric, results['p'], results['r'], results['f']))
        print()