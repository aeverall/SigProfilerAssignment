from SigProfilerAssignment import decomposition as decomp

def decompose_fit(samples,  output, signatures=None, signature_database=None,nnls_add_penalty=0.05, nnls_remove_penalty=0.01, initial_remove_penalty=0.05,genome_build="GRCh37",  make_decomposition_plots=True, collapse_to_SBS96=True,connected_sigs=True, verbose=False,devopts=None):

                decomp.spa_analyze(samples=samples,  output=output, signatures=signatures, signature_database=signature_database,nnls_add_penalty=nnls_add_penalty, nnls_remove_penalty=nnls_remove_penalty, initial_remove_penalty=initial_remove_penalty,genome_build=genome_build,  make_decomposition_plots=make_decomposition_plots, collapse_to_SBS96=collapse_to_SBS96,connected_sigs=connected_sigs, verbose=verbose,decompose_fit_option= True,denovo_refit_option=False,cosmic_fit_option=False,devopts=devopts)

def denovo_fit(samples,  output, signatures=None, signature_database=None,nnls_add_penalty=0.05,nnls_remove_penalty=0.01, initial_remove_penalty=0.05, genome_build="GRCh37",  make_decomposition_plots=True, collapse_to_SBS96=True,connected_sigs=True, verbose=False,devopts=None):
                decomp.spa_analyze(samples=samples,  output=output, signatures=signatures, signature_database=signature_database,nnls_add_penalty=nnls_add_penalty, nnls_remove_penalty=nnls_remove_penalty, initial_remove_penalty=initial_remove_penalty,genome_build=genome_build,  make_decomposition_plots=make_decomposition_plots, collapse_to_SBS96=collapse_to_SBS96,connected_sigs=connected_sigs, verbose=verbose,decompose_fit_option= False,denovo_refit_option=True,cosmic_fit_option=False,devopts=devopts)

def cosmic_fit(samples,  output, signatures=None, signature_database=None,nnls_add_penalty=0.05, nnls_remove_penalty=0.01, initial_remove_penalty=0.05,genome_build="GRCh37",  make_decomposition_plots=True, collapse_to_SBS96=True,connected_sigs=True, verbose=False,devopts=None):
                decomp.spa_analyze(samples=samples,  output=output, signatures=signatures, signature_database=signature_database,nnls_add_penalty=nnls_add_penalty, nnls_remove_penalty=nnls_remove_penalty, initial_remove_penalty=initial_remove_penalty,genome_build=genome_build,  make_decomposition_plots=make_decomposition_plots, collapse_to_SBS96=collapse_to_SBS96,connected_sigs=connected_sigs, verbose=verbose,decompose_fit_option= False,denovo_refit_option=False,cosmic_fit_option=True,devopts=devopts)