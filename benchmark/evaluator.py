"""
Side-by-Side Benchmark Evaluator
"""

from agents.pipeline import VariantForgePipeline
from alphagenome.model_sim import AlphaGenomePredictor

class BenchmarkRunner:
    def __init__(self):
        self.vf = VariantForgePipeline()
        self.ag = AlphaGenomePredictor()

    def compare(self, gene: str, variant: str):
        ag_res = self.ag.predict(gene, variant)
        vf_res = self.vf.run_target(gene, variant)

        print(f"\n{'='*75}")
        print(f" SIDE-BY-SIDE BENCHMARK: {gene} ({variant})".center(75))
        print(f"{'='*75}")
        
        ag_avi = f"AVI: {ag_res['avi_pathogenicity']:.3f} | Splice: {ag_res['splice_site_shift']:.2f}"
        vf_val = f"Validated: {vf_res['agent2']['validated_target']} (Score: {vf_res['agent2']['top_disease_score']})"
        vf_cb = f"Halted: {vf_res['circuit_breaker_triggered']}"
        vf_cand = f"{vf_res['candidates_generated']} Candidate(s)" if not vf_res['circuit_breaker_triggered'] else "N/A (Compute Saved)"

        table = [
            f"| {'Dimension':<25} | {'AlphaGenome (DeepMind)':<26} | {'VariantForge (Multi-Agent)':<28} |",
            f"|{'-'*27}|{'-'*28}|{'-'*30}|",
            f"| {'Primary Input Scope':<25} | {'1 Mb DNA Sequence Window':<26} | {'Gene + Variant Identifier':<28} |",
            f"| {'Variant Effect Metric':<25} | {ag_avi:<26} | {vf_res['agent1']['classification'].upper():<28} |",
            f"| {'Target Disease Score':<25} | {'Manual Lookup Required':<26} | {vf_val:<28} |",
            f"| {'Circuit Breaker Halted':<25} | {'No (Predictive Only)':<26} | {vf_cb:<28} |",
            f"| {'Drug SMILES Generated':<25} | {'None (0 Therapeutics)':<26} | {vf_cand:<28} |"
        ]
        print("\n".join(table))

if __name__ == "__main__":
    runner = BenchmarkRunner()
    runner.compare("PCSK9", "Q152H")
    runner.compare("PNPLA3", "I148M")
    runner.compare("HSD17B13", "rs72613567")