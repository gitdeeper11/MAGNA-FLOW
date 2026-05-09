#!/usr/bin/env python3
"""
MAGNA-FLOW Control Runner - Pure Python
"""

import sys
import os
import argparse

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from magna_flow import MHDStateTracker, MagnaFlowEngine


def main():
    parser = argparse.ArgumentParser(description="MAGNA-FLOW MHD Control")
    parser.add_argument("--regime", type=str, default="tokamak_elm",
                        choices=["tokamak_elm", "hall_thruster", "liquid_metal", "dynamo_analog"])
    parser.add_argument("--steps", "-s", type=int, default=1000)
    parser.add_argument("--verbose", "-v", action="store_true")
    
    args = parser.parse_args()
    
    print("=" * 60)
    print("MAGNA-FLOW (E-LAB-09) - Neural MHD Dissipation Control")
    print("=" * 60)
    
    engine = MagnaFlowEngine(regime=args.regime)
    result = engine.run_control_campaign(duration_ms=100.0)
    
    print(f"\nRegime: {args.regime}")
    print(f"η_MHD (Efficiency): {result.mean_efficiency*100:.1f}%")
    print(f"Dissipation Reduction: {result.dissipation_reduction*100:.1f}%")
    
    if args.regime == "tokamak_elm":
        print(f"ELM Suppression: {result.elm_suppression:.1f}×")
    elif args.regime == "hall_thruster":
        print(f"Isp Gain: +{result.isp_gain_seconds:.0f} seconds")
    
    print("\n✅ Control campaign complete")
    return 0


if __name__ == "__main__":
    sys.exit(main())
